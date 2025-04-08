from django.contrib import admin
from .models import Producto
from .forms import ProductoForm

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
    list_display = ('nombre', 'categoria', 'subcategoria', 'destacado')
    list_filter = ('categoria', 'subcategoria', 'destacado')
