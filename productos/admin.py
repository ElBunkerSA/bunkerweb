from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('nombre', 'descripcion')
