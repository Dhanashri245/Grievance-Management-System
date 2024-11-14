# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Complaint

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','role']
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        if len(password1) < 8:  # Custom validation for password length
            raise forms.ValidationError("This password is too short. It must contain at least 8 characters.")
        
from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'complaint_text', 'photo']  # Ensure these fields match your model