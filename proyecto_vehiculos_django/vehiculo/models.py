from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Vehiculo(models.Model):

    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet','Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota')
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, blank=True, default='Ford')

    modelo = models.CharField(max_length=100)

    serial_carroceria = models.CharField(max_length=50)

    serial_motor = models.CharField(max_length=50)

    CATEGORIAS =[
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    ]

    categoria = models.CharField(max_length=20, choices=CATEGORIAS, blank=True, default='P')

    precio = models.FloatField(null=False)

    fecha_creacion = models.DateField(auto_now_add=True)

    fecha_modificacion = models.DateField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)

    class Meta:
        ordering = ['marca', 'modelo']

    def get_absolute_url(self):
        return reverse('state', args=[str(self.id)])
    
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, precio: {self.precio}"