from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('collection/<int:pk>/', views.collectioin_detail, name='collectioin_detail'),
]