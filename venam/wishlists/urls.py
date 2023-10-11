from django.urls import path
from .views import WishlistView, wishlist_add, wishlist_remove
from django.contrib.auth.decorators import login_required

app_name = 'wishlists'

urlpatterns = [
    path('', login_required(WishlistView.as_view()), name='wishlist'),
    path('add/<int:product_id>/', wishlist_add, name='wishlist_add'),
    path('remove/<int:wishlist_id>/', wishlist_remove, name='wishlist_remove'),
    ]