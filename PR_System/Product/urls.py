from django.urls import path
from .views import *

urlpatterns = [
    path('product/', product_list, name='Product_view'),
    path('add_product/', add_product, name='Add_Product'),
    path('product/edit/<int:id>/', edit_product, name='Edit_Product'),
    path('product/delete/<int:id>/', delete_product, name='Delete_Product'),
    path('register/', RegisterView.as_view(), name='user-register'),
]
