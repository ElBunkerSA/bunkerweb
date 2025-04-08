from django.shortcuts import render
from .models import Producto

def index(request):
    # Destacados: sin importar categoría, solo destacados.
    destacados = Producto.objects.filter(destacado=True)

    # Periféricos
    ratones = Producto.objects.filter(categoria='perifericos', subcategoria='ratones')
    mandos = Producto.objects.filter(categoria='perifericos', subcategoria='mandos')
    teclados = Producto.objects.filter(categoria='perifericos', subcategoria='teclados')
    cascos = Producto.objects.filter(categoria='perifericos', subcategoria='cascos')

    # Videojuegos
    videojuegos_fisicos = Producto.objects.filter(categoria='videojuegos', subcategoria='fisico')
    videojuegos_digitales = Producto.objects.filter(categoria='videojuegos', subcategoria='digital')

    # Hardware y Consolas
    consolas = Producto.objects.filter(categoria='hardware', subcategoria='consolas')
    pc = Producto.objects.filter(categoria='hardware', subcategoria='pc')
    componentes = Producto.objects.filter(categoria='hardware', subcategoria='componentes')

    # Otros
    otros = Producto.objects.filter(categoria='otros')

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
