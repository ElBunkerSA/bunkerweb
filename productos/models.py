from django.db import models

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('perifericos', 'Periféricos'),
        ('videojuegos', 'Videojuegos'),
        ('hardware', 'Hardware y Consolas'),
        ('otros', 'Otros'),
    ]
    SUBCATEGORIA_PERIFERICOS = [
        ('ratones', 'Ratones'),
        ('mandos', 'Mandos'),
        ('teclados', 'Teclados'),
        ('cascos', 'Cascos'),
    ]
    SUBCATEGORIA_VIDEOJUEGOS = [
        ('fisicos', 'Físicos'),
        ('digitales', 'Digitales'),
    ]
    SUBCATEGORIA_HARDWARE = [
        ('consolas', 'Consolas'),
        ('pc', 'PC'),
        ('componentes', 'Componentes'),
    ]
    SUBCATEGORIA_CHOICES = SUBCATEGORIA_PERIFERICOS + SUBCATEGORIA_VIDEOJUEGOS + SUBCATEGORIA_HARDWARE

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='otros')
    subcategoria = models.CharField(max_length=20, choices=SUBCATEGORIA_CHOICES, null=True, blank=True,
                                    help_text="Selecciona la subcategoría según la categoría principal")
    imagen_url = models.URLField(verbose_name="URL de la imagen")
    afiliado_url = models.URLField(verbose_name="URL de afiliado")
    descripcion = models.TextField(verbose_name="Descripción (por qué recomendamos el producto)")
    destacado = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0, help_text="Número de orden, menor se muestra primero")

    def __str__(self):
        return self.nombre
