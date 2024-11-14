from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import UserRegisterForm,ComplaintForm
from .models import CustomUser,Complaint  # Ensure Complaint is imported correctly# Import your CustomUser model
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # Check if the email already exists
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'This email is already in use. Please use a different email.')
                return render(request, 'register.html', {'form': form})

            user = form.save(commit=False)  # Create user instance but don't save yet
            user.role = form.cleaned_data.get('role')  # Set the user role
            user.save()  # Now save the user
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page
        else:
            print("Form errors:", form.errors)  # Debugging line
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name= 'login.html'
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            # Check the user's role and redirect accordingly
            if user.role == 'admin':
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            elif user.role == 'employee':
                return redirect('employee_dashboard')  # Redirect to employee dashboard
            elif user.role == 'user':
                return redirect('user_dashboard')  # Redirect to user dashboard
            else:
                return redirect('home')  # Default redirect
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')  # Ensure you have a login.html template
def home_view(request):
    return render(request, 'home.html')  # Ensure you have a home.html template

# views.py
@login_required
def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')  # Create this template

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')  # Create this template

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')  # Ensure you have this template


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ComplaintForm

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)  # Pass POST and FILES data to the form
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Your complaint has been submitted successfully!')
            return redirect('user_dashboard')  # Redirect back to the user dashboard
        else:
            # If the form is not valid, print the errors for debugging
            messages.error(request, 'There was an error with your submission.')
            print(form.errors)  # Print form errors for debugging
            return render(request, 'user_dashboard.html', {'form': form})  # Render the form again with errors
    else:
        # If the request method is not POST, redirect to the user dashboard
        return redirect('user_dashboard')