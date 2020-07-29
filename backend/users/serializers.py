from rest_framework import serializers
from .models import User, UserToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


class RegistrationSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(
    #     max_length=128,
    #     min_length=8,
    #     write_only=True
    # )

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id', 'first_name', 'last_name',
                  'email', 'is_active', 'is_staff', 'is_registered', 'user_type', 'business_unit']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    exp_time = serializers.IntegerField(read_only=True)
    is_active = serializers.CharField(read_only=True)
    status = serializers.IntegerField(read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError("Email is required to login")

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.')

        user_obj = get_object_or_404(User, email=email)

        # if not user_obj.is_active:
        #     raise serializers.ValidationError(
        #         'User login has been disabled. Please contact administrator.'
        #     )
        if not user_obj.is_active:
            return {
                'status': 400,
                'email': '',
                'token': '',
                'exp_time': 1
            }

        user = authenticate(username=email, password=password)
        # print(user)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )

        return {
            'email': user.email,
            'is_active': user.is_active,
            'token': user.token['token'],
            'exp_time': user.token['exp_time'],
            'status': 200
        }


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name', 'is_active', 'is_staff', 'is_registered',
                  'business_unit', 'user_type']

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class UserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToken
        fields = '__all__'

    def create(self, validated_data):

        # print(validated_data)
        userId = validated_data['user']
        token = validated_data['token']
        user_token = UserToken.objects.create(user=userId, token=token)
        return user_token


class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active', "is_registered",
                  "user_type", "business_unit"]
