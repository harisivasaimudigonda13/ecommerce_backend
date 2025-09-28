from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from cart.models import Cart

@api_view(['GET'])
def dashboard_stats(request):
    data = {
        "products": Product.objects.count(),
        "users": User.objects.count(),
        "cart": Cart.objects.count(),
    }
    return Response(data)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # sir code
# @api_view([;GET])
# def product_list(request):
#     print("Products List API called")
#     serialized = ProductSerializer(Product.objects.all(),many =True)
#     return Response(serialized.data)