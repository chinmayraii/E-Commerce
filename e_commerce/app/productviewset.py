from rest_framework import viewsets
from . models import Product
from .productserializer import ProductSeralizer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSeralizer