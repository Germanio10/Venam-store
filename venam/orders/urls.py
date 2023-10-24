from django.urls import path
from .views import OrderCreateView, OrderCompletedView


app_name = 'orders'

urlpatterns = [
    path('', OrderCreateView.as_view(), name='order-create'),
    path('order-completed/', OrderCompletedView.as_view(), name='complete')
]
