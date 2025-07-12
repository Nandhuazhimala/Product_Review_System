from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import ProductSerializer,RegisterSerializer,LoginSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



# Create your views here.

# show products


@api_view(['GET'])
@permission_classes([])
def product_list(request):
    product_obj = Products.objects.all()
    serializer_data = ProductSerializer(product_obj, many=True)
    return Response(serializer_data.data)

# add products

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_product(request):
    product_data=request.data
    serializer_data = ProductSerializer(data=product_data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)
    return Response(serializer_data.errors, status=status.HTTP_404_NOT_FOUND)

# Edit Product data

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_product(request, id):
    try:
         product_data=request.data
         product_obj = Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response({'error': 'Product data not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer_data = ProductSerializer( product_obj, data=product_data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data)
    return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete product data

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, id):
    try:
         product_obj = Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    product_obj.delete()
    return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# User Register section 
@permission_classes([])
class RegisterView(APIView):
    def post(self, request):
        user_data = request.data
        serializer = RegisterSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Login Section
@permission_classes([])
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'message': 'Login successful',
            'token': str(token),
            'username': user.username,
            'is_admin': user.is_staff
        }, status=status.HTTP_200_OK)
    
# Logout Section

@permission_classes([])
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        return Response({"error": "User not authenticated"}, status=status.HTTP_404_NOT_FOUND)