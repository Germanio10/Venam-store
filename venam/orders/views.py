from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import OrderForm


class OrderCreateView(CreateView):
    template_name = 'orders/order.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:complete')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
    

class OrderCompletedView(TemplateView):
    template_name = 'orders/order-completed.html'
