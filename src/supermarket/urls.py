from rest_framework import routers

from .views import SupermarketViewSet, ProductViewSet, ProductTypeViewSet, GroceryListViewSet

router = routers.DefaultRouter()
router.register(r'shop', SupermarketViewSet, base_name='shop')
router.register(r'product', ProductViewSet, base_name='product')
router.register(r'product-type', ProductTypeViewSet, base_name='product-type')
router.register(r'grocery-list', GroceryListViewSet, base_name='grocery-list')

urlpatterns = router.urls