from rest_framework import serializers
from .models import *

# Create for product serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"
