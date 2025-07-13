from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# Create for product serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"

# create register section

class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
    
# create login section

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


# Review Section

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'review', 'created_at']




