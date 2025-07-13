from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='Product_view'),
    path('add_product/', add_product, name='Add_Product'),
    path('product/edit/<int:id>/', edit_product, name='Edit_Product'),
    path('product/delete/<int:id>/', delete_product, name='Delete_Product'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('product/add_review/<int:id>/', add_review, name='Add_Review'),
    path('product/reviews/<int:id>/', product_review, name='Product_Review'),
]
