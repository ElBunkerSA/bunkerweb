from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField  # Importa el campo de selección múltiple

class Producto(models.Model):
    # Opciones de categorías y subcategorías
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

    # Opciones para plataformas del producto
    PLATAFORMA_CHOICES = [
        ('PC', 'PC'),
        ('SWITCH', 'Switch'),
        ('PS5', 'PS5'),
        ('XBOX', 'Xbox'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='otros')
    subcategoria = models.CharField(
        max_length=20,
        choices=SUBCATEGORIA_CHOICES,
        null=True,
        blank=True,
        help_text="Selecciona la subcategoría según la categoría principal"
    )
    imagen_url = models.URLField(verbose_name="URL de la imagen")
    afiliado_url = models.URLField(verbose_name="URL de afiliado")
    descripcion = models.TextField(verbose_name="Descripción (por qué recomiendas el producto)")
    destacado = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=50, help_text="Número de orden; menor se muestra primero")
    # Nuevos campos:
    plataformas = MultiSelectField(choices=PLATAFORMA_CHOICES, blank=True, null=True, help_text="Selecciona las plataformas para las cuales es válido el producto")
    descuento = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Descuento actual (0-100)"
    )

    def __str__(self):
        return self.nombre
