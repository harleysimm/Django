from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','username','is_active')
    list_filter = ('last_name', 'is_active', 'is_superuser')
    fields = ('email', 'first_name', 'last_name', 'is_superuser')

admin.site.register(User, UserAdmin)
    

