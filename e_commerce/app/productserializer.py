from dataclasses import fields
from rest_framework import serializers
from . models import Product

class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['title','selling_price','discounted_price','description','brand','category','product_image']