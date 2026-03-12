from django.contrib import admin

from main_app.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'is_active']
    search_fields = ['full_name', 'email']