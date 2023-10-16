from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from products.models import Product
from .models import Cart
from django.urls import reverse


class CartlistView(ListView):
    template_name = 'carts/cart.html'
    model = Cart


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.filter(user=request.user, product=product)

    if not cart.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = cart.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(reverse('carts:cart'))


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
