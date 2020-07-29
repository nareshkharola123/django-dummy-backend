from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from bayview.jwt_authentication import JWTAuthentication
from bayview.renders import UserJSONRenderer
from consumers.serializers import ConsumerSerializer
from consumers.service.consumer_service import ConsumerService
from bayview.permission import AdminLevelPermission

# Create your views here.


class ConsumerViewSet(viewsets.ModelViewSet):
    """
    ref: jira-BWM-92
    """

    queryset = ConsumerService().consumer_all()
    serializer_class = ConsumerSerializer
    permission_classes = []
    authentication_classes = []
    # renderer_classes = (UserJSONRenderer,)

    def list(self, request):
        queryset = ConsumerService().consumer_all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            consumer = ConsumerService().consumer_add_client_and_secret_key(serializer.data)  # NOQA
            serializer = self.serializer_class(consumer)
        else:
            return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": serializer.data},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        response = ConsumerService().consumer_deactive(pk)
        return Response(response, status=status.HTTP_200_OK)
