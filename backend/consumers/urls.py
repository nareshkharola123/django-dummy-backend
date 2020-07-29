from rest_framework.routers import DefaultRouter
from .views import ConsumerViewSet

router = DefaultRouter()

router.register(r'', ConsumerViewSet, basename='consumer')
urlpatterns = router.urls
