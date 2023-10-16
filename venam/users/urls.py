from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileUpdateView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile')
]