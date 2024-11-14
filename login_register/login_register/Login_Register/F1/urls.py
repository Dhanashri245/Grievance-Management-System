# urls.py
from django.contrib import admin
from django.urls import path
from .views import register, login_view
from django.contrib.auth.views import LogoutView
from .views import home_view, admin_dashboard,employee_dashboard,user_dashboard,submit_complaint

from django.urls import path
from .views import register, login_view, home_view, admin_dashboard, employee_dashboard, user_dashboard, submit_complaint
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),  # Home page
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    #path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('employee-dashboard/', employee_dashboard, name='employee_dashboard'),
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
    path('submit-complaint/', submit_complaint, name='submit_complaint'),  # Complaint submission
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)