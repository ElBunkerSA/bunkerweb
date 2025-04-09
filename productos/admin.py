from django.contrib import admin
from .models import Producto
from .forms import ProductoForm

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm  # o puedes usar el formulario por defecto
    list_display = ('nombre', 'categoria', 'subcategoria', 'destacado', 'orden')
    list_filter = ('categoria', 'subcategoria', 'destacado')
    ordering = ('orden',)  # Esto obliga a ordenar en el admin
