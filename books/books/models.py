from django.db import models
from django.urls import reverse
from users.models import User


class Book(models.Model):
    
    titulo= models.CharField(max_length=100)
    editorial= models.CharField(max_length=20)

    STATUS = (
        ('A', 'Activo'),
        ('M', 'Mantenimiento'),
        ('R', 'Reservado')

    )
    state = models.CharField(max_length=1, choices=STATUS, blank=True, default='A')

    TIPOS_BOOK = [
        ('E', 'Empastado'),
        ('D', 'Digital')
    ]

    type = models.CharField(max_length=1, choices=TIPOS_BOOK, blank=True, default='E')

    COLOR_FAVORITO = [
        (1, 'Azul'),
        (2, 'Negro'),
        (3, 'Blanco'),
        (4, 'Gris')
    ]

    preferencia = models.CharField(max_length=200, choices=COLOR_FAVORITO, blank=True, default='')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)



    class Meta:
        ordering = ["titulo", "editorial", "state"]
        
    
    def get_absolute_url(self):
        return reverse("state", args=[str(self.id)])
        
    def __str__(self):
        return f"titulo: {self.titulo}, editorial: {self.editorial}, status: {self.state}"
