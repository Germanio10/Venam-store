from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserLoginForm
from django.urls import reverse_lazy


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class =  UserRegistrationForm
    success_url = reverse_lazy('index')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')