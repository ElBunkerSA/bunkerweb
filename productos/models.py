from django.db import models

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('perifericos', 'Periféricos'),
        ('videojuegos', 'Videojuegos'),
        ('hardware', 'Hardware y Consolas'),
        ('otros', 'Otros'),
    ]
    # Subcategorías para cada grupo:
    SUBCATEGORIA_PERIFERICOS = [
        ('ratones', 'Ratones'),
        ('mandos', 'Mandos'),
        ('teclados', 'Teclados'),
        ('cascos', 'Cascos'),
    ]
    SUBCATEGORIA_VIDEOJUEGOS = [
        ('fisico', 'Físicos'),
        ('digital', 'Digitales'),
    ]
    SUBCATEGORIA_HARDWARE = [
        ('consolas', 'Consolas'),
        ('pc', 'PC'),
        ('componentes', 'Componentes'),
    ]
    # Se crea una lista general de todas las subcategorías
    SUBCATEGORIA_CHOICES = SUBCATEGORIA_PERIFERICOS + SUBCATEGORIA_VIDEOJUEGOS + SUBCATEGORIA_HARDWARE

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES if False else CATEGORIA_CHOICES, default='otros')  # Nota: aquí usaremos el campo "categoria" para la categoría principal; aunque usualmente se definen choices, en este caso optamos por no atarlo directamente, ya que la subcategoría dependerá de la categoría.
    # Opcional: Puedes quitar choices en subcategoria para que cada producto seleccione libremente según su categoría;
    # o bien, usar la unión de todas las opciones para guiarlos:
    subcategoria = models.CharField(max_length=20, choices=SUBCATEGORIA_CHOICES, null=True, blank=True,
                                    help_text="Seleccione la subcategoría según la categoría principal")
    imagen_url = models.URLField(verbose_name="URL de la imagen")
    afiliado_url = models.URLField(verbose_name="URL de afiliado")
    descripcion = models.TextField(verbose_name="Descripción (por qué recomiendas el producto)")
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
