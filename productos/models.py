from django.db import models


class Producto(models.Model):
    TIPO_CHOICES = [
        ('juegos', 'Juegos'),
        ('ratones', 'Ratones'),
        ('teclados', 'Teclados'),
        ('mandos', 'Mandos'),
        ('cascos', 'Cascos'),
        ('otros', 'Otros'),
    ]
    SUBTIPO_JUEGOS = [
        ('fisico', 'Juegos Físicos'),
        ('digital', 'Juegos Digitales'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    imagen_url = models.URLField(verbose_name="URL de la imagen")
    afiliado_url = models.URLField(verbose_name="URL de afiliado")
    descripcion = models.TextField(verbose_name="Descripción (por qué recomiendas el producto)")
    destacado = models.BooleanField(default=False)
    # Este campo sólo se usará cuando el tipo sea 'juegos'
    subcategoria = models.CharField(
        max_length=10, choices=SUBTIPO_JUEGOS, null=True, blank=True,
        help_text="Usar sólo si el tipo es 'juegos'."
    )

    def __str__(self):
        return self.nombre
