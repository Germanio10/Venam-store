from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.urls import reverse_lazy
from .models import User


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')


class ProfileUpdateView(UpdateView):
    template_name = 'users/profile.html'
    model = User
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id, ))
