from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import AdminRegistrationForm, AdminLoginForm,CustomUserCreationForm



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_admin')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'admin/register_admin.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')  # Redirect to admin dashboard or any other page
    else:
        form = AdminLoginForm()
    return render(request, 'admin/login_admin.html', {'form': form})
# accounts/views.py
from django.contrib.auth.decorators import login_required


def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')