from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Supermarket, Product, ProductType, GroceryList
from .serializers import SupermarketSerializer, SupermarketProductSerializer, \
    SupermarketProductTypeSerializer, SupermarketGroceryListSerializer


class SupermarketViewSet(viewsets.ViewSet, ModelViewSet):
    serializer_class = SupermarketSerializer
    queryset = Supermarket.objects.all()


class ProductViewSet(viewsets.ViewSet, ModelViewSet):
    serializer_class = SupermarketProductSerializer
    queryset = Product.objects.all()


class ProductTypeViewSet(viewsets.ViewSet, ModelViewSet):
    serializer_class = SupermarketProductTypeSerializer
    queryset = ProductType.objects.all()


class GroceryListViewSet(viewsets.ViewSet, ModelViewSet):
    serializer_class = SupermarketGroceryListSerializer
    queryset = GroceryList.objects.all()

