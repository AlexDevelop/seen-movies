from rest_framework import routers

from .views import MoviesViewSet

router = routers.DefaultRouter()
router.register(r'', MoviesViewSet, base_name='movies')

urlpatterns = router.urls