from django.shortcuts import render
from .models import Producto

def index(request):
    context = {
        'ratones': Producto.objects.filter(tipo='raton'),
        'teclados': Producto.objects.filter(tipo='teclado'),
        'mandos': Producto.objects.filter(tipo='mando'),
        'monitores': Producto.objects.filter(tipo='monitor'),
        'cascos': Producto.objects.filter(tipo='casco'),
    }
    return render(request, 'productos/index.html', context)
