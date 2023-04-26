from django.urls import path
from .views import CategoryView, ItemView, OrderView

app_name = 'shop'

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category-detail'),
    path('category/<int:pk>/item/', ItemView.as_view(), name='item-list'),
    path('category/<int:pk>/item/<int:item_pk>/', ItemView.as_view(), name='item-detail'),
    path('category/<int:pk>/item/<int:item_pk>/order/', OrderView.as_view(), name='order-list'),
    path('category/<int:pk>/item/<int:item_pk>/order/<int:order_pk>/', OrderView.as_view(), name='order-detail'),
]