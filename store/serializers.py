from decimal import Decimal
from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "product_count"]
        
    product_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "inventory",
            "unit_price",
            "collection",
            "price_with_tax",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
