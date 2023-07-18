from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
from articulos.models import Articulo

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')

admin.site.register(User, UserAdmin)

