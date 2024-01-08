from django.contrib import admin

# Register your models here.
from .models import CustomerUser

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id', 'first_name', 'last_name', 'is_active', 'mobile', 'address')

