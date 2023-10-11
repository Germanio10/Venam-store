from django.urls import path
from .views import CartlistView, cart_add, cart_remove
from django.contrib.auth.decorators import login_required

app_name = 'carts'

urlpatterns = [
    path('', login_required(CartlistView.as_view()), name='cart'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
