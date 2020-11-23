from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from .models import UserManager, User



class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'name', 'phone', 'email', 'permissions',
                 'remark', 'is_active', 'last_login', 'create_date', 'is_superuser']
	search_fields = ['username']





admin.site.register(User, UserAdmin)

