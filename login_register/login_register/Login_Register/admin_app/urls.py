# accounts/urls.py
from django.urls import path
from .views import register, admin_login,admin_dashboard

urlpatterns = [
    path('register/', register, name='register_admin'),
    path('login/', admin_login, name='login_admin'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]