from django.db import models


class Producto(models.Model):
    TIPO_CHOICES = [
        ('raton', 'Ratón'),
        ('teclado', 'Teclado'),
        ('mando', 'Mando'),
        ('casco', 'Casco'),
        ('monitor', 'Monitor'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    imagen_url = models.URLField(verbose_name="URL de la imagen")
    afiliado_url = models.URLField(verbose_name="URL de afiliado")
    descripcion = models.TextField(verbose_name="Descripción (por qué recomiendas el producto)")

    def __str__(self):
        return self.nombre
