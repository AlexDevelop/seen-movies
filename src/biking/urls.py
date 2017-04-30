from rest_framework import routers

from .views import BikeRideViewSet

router = routers.DefaultRouter()
router.register(r'', BikeRideViewSet, base_name='biking')

urlpatterns = router.urls