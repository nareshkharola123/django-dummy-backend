
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import BusinessUnitSerializer
from bayview.jwt_authentication import JWTAuthentication
from .service.business_unit_service import BusinessUnitService
from bayview.permission import AdminLevelPermission
from bayview.renders import UserJSONRenderer

# Create your views here.


class BusinessUnitViewSet(viewsets.ModelViewSet):
    """
    Jira ref: BWM-91
    """
    queryset = BusinessUnitService().business_unit_all()
    serializer_class = BusinessUnitSerializer
    permission_classes = []  # AdminLevelPermission to check user is admin  # NOQA
    authentication_classes = []
    # renderer_classes = (UserJSONRenderer,)

    def list(self, request):
        queryset = BusinessUnitService().business_unit_all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        response = BusinessUnitService().delete_business_unit_object(pk)
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = request.data
        response = BusinessUnitService().check_update_business_unit_object(pk, data)  # NOQA
        return Response(response, status=status.HTTP_200_OK)
