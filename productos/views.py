from django.shortcuts import render
from .models import Producto

def index(request):
    destacados = Producto.objects.filter(destacado=True).order_by('orden', '-fecha_creacion')

    # Periféricos: filtrado por subcategorías
    ratones = Producto.objects.filter(categoria='perifericos', subcategoria='ratones').order_by('orden', '-fecha_creacion')
    mandos = Producto.objects.filter(categoria='perifericos', subcategoria='mandos').order_by('orden', '-fecha_creacion')
    teclados = Producto.objects.filter(categoria='perifericos', subcategoria='teclados').order_by('orden', '-fecha_creacion')
    cascos = Producto.objects.filter(categoria='perifericos', subcategoria='cascos').order_by('orden', '-fecha_creacion')

    # Videojuegos
    videojuegos_fisicos = Producto.objects.filter(categoria='videojuegos', subcategoria='fisicos').order_by('orden', '-fecha_creacion')
    videojuegos_digitales = Producto.objects.filter(categoria='videojuegos', subcategoria='digitales').order_by('orden', '-fecha_creacion')

    # Hardware y Consolas
    consolas = Producto.objects.filter(categoria='hardware', subcategoria='consolas').order_by('orden', '-fecha_creacion')
    pc = Producto.objects.filter(categoria='hardware', subcategoria='pc').order_by('orden', '-fecha_creacion')
    componentes = Producto.objects.filter(categoria='hardware', subcategoria='componentes').order_by('orden', '-fecha_creacion')

    # Otros
    otros = Producto.objects.filter(categoria='otros').order_by('orden', '-fecha_creacion')

    context = {
        'destacados': destacados,
        'ratones': ratones,
        'mandos': mandos,
        'teclados': teclados,
        'cascos': cascos,
        'videojuegos_fisicos': videojuegos_fisicos,
        'videojuegos_digitales': videojuegos_digitales,
        'consolas': consolas,
        'pc': pc,
        'componentes': componentes,
        'otros': otros,
    }
    return render(request, 'productos/index.html', context)
