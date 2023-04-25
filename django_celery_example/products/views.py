from django.db.models import F, ExpressionWrapper, DecimalField
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.annotate(
        discounted_price_annotated=ExpressionWrapper(F('price') * 0.5, output_field=DecimalField())
    )
    serializer_class = ProductSerializer

