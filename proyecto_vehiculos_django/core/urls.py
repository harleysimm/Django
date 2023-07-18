from vehiculo import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vehiculo/', include("vehiculo.urls")),
    path('accounts/', include('django.contrib.auth.urls'))
]
