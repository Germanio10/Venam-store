from .models import Cart

def cart_context(request):
    if request.user.is_authenticated:
        cart_products = Cart.objects.filter(user=request.user)
        total_sum = sum(cart.product.price * cart.quantity for cart in cart_products)
    else:
        cart_products = []
        total_sum = 0
    
    context = {
        'cart_products': cart_products,
        'total_sum': total_sum
    }
    return context
