from django.shortcuts import render
from .models import Producto


def index(request):
    destacados = Producto.objects.filter(destacado=True)
    juegos_fisicos = Producto.objects.filter(tipo='juegos', subcategoria='fisico')
    juegos_digitales = Producto.objects.filter(tipo='juegos', subcategoria='digital')
    ratones = Producto.objects.filter(tipo='ratones')
    teclados = Producto.objects.filter(tipo='teclados')
    mandos = Producto.objects.filter(tipo='mandos')
    cascos = Producto.objects.filter(tipo='cascos')
    otros = Producto.objects.filter(tipo='otros')

    context = {
        'destacados': destacados,
        'juegos_fisicos': juegos_fisicos,
        'juegos_digitales': juegos_digitales,
        'ratones': ratones,
        'teclados': teclados,
        'mandos': mandos,
        'cascos': cascos,
        'otros': otros,
    }
    return render(request, 'productos/index.html', context)
