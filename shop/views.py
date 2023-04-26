from rest_framework import generics
from .models import Category, Item, Order
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer

class CategoryView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer