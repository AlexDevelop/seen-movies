from rest_framework import serializers

from .models import Supermarket, Product, ProductType, GroceryList


class SupermarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supermarket
        fields = ('id', 'name', )


class SupermarketProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'name', )


class SupermarketProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'product_type')


class SupermarketGroceryListSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    supermarket_name = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.amount * obj.product.price

    def get_supermarket_name(self, obj):
        return obj.supermarket.name

    class Meta:
        model = GroceryList
        fields = ('id', 'amount', 'product', 'supermarket', 'total_price', 'supermarket_name')
