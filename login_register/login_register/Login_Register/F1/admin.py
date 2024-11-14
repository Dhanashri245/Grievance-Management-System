from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import CustomUser,Complaint

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  # Fields to display in the admin list view
    list_filter = ('role', 'is_staff', 'is_active')  # Filters for the admin list view
    search_fields = ('username', 'email')  # Searchable fields
class ComplaintAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'complaint_text', 'photo')  # Fields to display in the admin list view
    search_fields = ('name', 'email')  # Searchable fields
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Complaint, ComplaintAdmin)