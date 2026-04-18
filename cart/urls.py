from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, UpdateCartItemView, ClearCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='cart-add'),
    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='cart-remove'),
    path('update/<int:item_id>/', UpdateCartItemView.as_view(), name='cart-update'),
    path('clear/', ClearCartView.as_view(), name='cart-clear'),
]
