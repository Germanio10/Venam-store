from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product
from .models import Wishlist


class WishlistView(ListView):
    template_name = 'wishlists/wishlist.html'
    model = Wishlist
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_wishlists = Wishlist.objects.filter(user=self.request.user)
        context['product_wishlists'] = product_wishlists
        return context
    


def wishlist_add(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist = Wishlist.objects.filter(user=request.user, product=product)

    if not wishlist.exists():
        Wishlist.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = wishlist.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def wishlist_remove(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    wishlist.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
