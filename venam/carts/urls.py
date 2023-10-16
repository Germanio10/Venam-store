from django.urls import path
from .views import CartlistView, cart_add, cart_remove

app_name = 'carts'

urlpatterns = [
    path('', CartlistView.as_view(), name='cart'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
