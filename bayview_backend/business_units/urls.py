from rest_framework.routers import DefaultRouter
from .views import BusinessUnitViewSet


router = DefaultRouter()

router.register(r'', BusinessUnitViewSet, basename='business_unit')

urlpatterns = router.urls
