from django.db import models
from django.urls import reverse

unit_selection = [('Kg', 'Kilos'),('Lts', 'Litros'),
                  ('Paq', 'Paquete'), ('Un', 'Unidad')]

class Articulo(models.Model):
    
    name= models.CharField(max_length=100)
    description= models.CharField(max_length=200)
    price= models.FloatField()
    stock= models.FloatField()
    unit= models.CharField( 
        null=False, blank=False,
        choices=unit_selection,
        max_length=10
    )
    largo= models.FloatField()
    ancho= models.FloatField()
    peso= models.FloatField()
    color= models.CharField(max_length=20)
    model= models.CharField(max_length=50)

    
    class Meta:
        ordering = ['name']
                   
    def get_absolute_url(self):
        return reverse("articulos", args=[str(self.id)])
        
    def __str__(self):
        return f"nombre: {self.name}, descripción: {self.description}, precio: {self.price}, stock: {self.stock}, unidad: {self.unit}, largo: {self.largo}, ancho: {self.ancho}, peso: {self.peso}, color: {self.color}, modelo:{self.model}"