from django.shortcuts import render
from .models import Producto

def index(request):
    destacados = Producto.objects.filter(destacado=True).order_by('orden')

    # Periféricos: filtrado por subcategorías
    ratones = Producto.objects.filter(categoria='perifericos', subcategoria='ratones').order_by('orden')
    mandos = Producto.objects.filter(categoria='perifericos', subcategoria='mandos').order_by('orden')
    teclados = Producto.objects.filter(categoria='perifericos', subcategoria='teclados').order_by('orden')
    cascos = Producto.objects.filter(categoria='perifericos', subcategoria='cascos').order_by('orden')

    # Videojuegos
    videojuegos_fisicos = Producto.objects.filter(categoria='videojuegos', subcategoria='fisicos').order_by('orden')
    videojuegos_digitales = Producto.objects.filter(categoria='videojuegos', subcategoria='digitales').order_by('orden')

    # Hardware y Consolas
    consolas = Producto.objects.filter(categoria='hardware', subcategoria='consolas').order_by('orden')
    pc = Producto.objects.filter(categoria='hardware', subcategoria='pc').order_by('orden')
    componentes = Producto.objects.filter(categoria='hardware', subcategoria='componentes').order_by('orden')

    # Otros
    otros = Producto.objects.filter(categoria='otros').order_by('orden')

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
