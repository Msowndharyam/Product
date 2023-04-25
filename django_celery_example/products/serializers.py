from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discounted_price_annotated = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'discounted_price_annotated')



