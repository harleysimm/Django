from django.urls import path
from . import views

urlpatterns =[
    path('', views.articulos_list),
    path('<int:pk>/', views.articulo_detail), #/books/id
    path('new', views.new_articulo), #/books/new
    path('<int:pk>/edit', views.edit_articulo), #/books/id
    path('<int:pk>/delete', views.delete_articulo) #/books/id
]