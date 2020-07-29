from uuid import uuid4

from django.shortcuts import get_object_or_404
from django.conf import settings as settings
from django.core.mail import send_mail
from django.utils import timezone
from django.core.exceptions import PermissionDenied, ValidationError
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from bayview.jwt_authentication import JWTAuthentication
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer, UserTokenSerializer, GetUsersSerializer

from .models import User, UserToken
from .utilities import send_email
from django.http import HttpResponseRedirect


class RegistrationAPIView(views.APIView):

    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    authentication_classes = []

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token = str(uuid4())
        data = {
            'user': serializer.data['id'],
            'email': serializer.data['email'],
            'token': token
        }
        # print('data --- ', data)
        user_token_serializer = UserTokenSerializer(data=data)
        user_token_serializer.is_valid(raise_exception=True)
        user_token_serializer.save()
        # print(user_token_serializer)
        userId = user_token_serializer.data['user']
        token = user_token_serializer.data['token']
        user_instance = get_object_or_404(User, id=userId)
        email = user_instance.email
        send_email(token=token, email=email)
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)


class ResendEmailAPIView(views.APIView):

    authentication_classes = []
    permission_classes = (AllowAny,)

    def post(self, request):
        user_email = request.data
        email = user_email['email']
        # print(email)
        user_instance = get_object_or_404(User, email=email)
        user_token_instance = get_object_or_404(UserToken, user=user_instance)
        token = user_token_instance.token
        send_email(token=token, email=user_email['email'])
        return Response({"Email Sent"}, status=status.HTTP_200_OK)


class LoginAPIView(views.APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        if serializer.data['status'] == 400:
            return Response({"error": 'User login has been disabled. Please contact administrator.', "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    authentication_classes = []

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        payload = request.data
        user = get_object_or_404(User, email=payload['email'])
        serializer = self.serializer_class(user, data=payload, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ForgotPassword(views.APIView):

    serializer_class = User
    permission_classes = (AllowAny,)
    authentication_classes = []

    def post(self, request):
        email_object = request.data
        # print(email_object, '11')

        try:
            user = get_object_or_404(User, email=email_object['email'])
        except:
            return Response({'email': "not valid"})
        token = str(uuid4())
        # user = validated_data.user
        data = {
            'user': user.id,
            'email': email_object['email'],             'token': token
        }
        # print(data)
        serializer = self.serializer_class(UserToken, data=data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)

            send_email(serializer.data['email'], serializer.data['token'])
            return Response({"Email has been sent kindly check your inbox"}, status=200)
        else:
            # print(serializer.errors)
            # print(serializer.errors)
            return Response(serializer.errors,  status=400)


class ValidateTokenAPIView(views.APIView):

    permission_classes = (AllowAny,)
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        token = kwargs['token']

        try:
            user_token = get_object_or_404(UserToken, token=token)

        except Exception:
            return Response({"Invalid Token"}, status=403)
        if (timezone.now() - user_token.created).seconds > 60000:
            return Response({'is_validated': False}, status=200)

        else:
            return Response({"is_validated": True}, status=200)


class SetPasswordAPIView(views.APIView):

    permission_classes = (AllowAny,)
    authentication_classes = []

    def post(self, request):
        data = request.data
        token = data['token']
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            message = "password and re-entered password doesn't match"
            raise ValidationError(message=message)
        else:
            user_token = get_object_or_404(UserToken, token=token)
            user = user_token.user
            # user = get_object_or_404(User, userId)
            user.set_password(password)
            setattr(user, 'is_active', True)
            setattr(user, 'is_registered', True)

            user.save()
        return Response({"status": "Password Set Successfully"}, status=200)


class GetUsersAPIView(views.APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = GetUsersSerializer
    # renderer_classes = ()

    def get(self, request):
        users = User.objects.all()
        serialized_users = self.serializer_class(users, many=True)
        return Response(serialized_users.data, status=200)
