from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=CartItem._meta.get_field("product").remote_field.model.objects.all(),
        source="product",
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ("id", "product", "product_id", "quantity", "total_price")

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ("id", "user", "items", "created_at")
        read_only_fields = ("user", "created_at")
