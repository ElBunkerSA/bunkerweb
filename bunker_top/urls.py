from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Administración Búnker'
admin.site.site_title = 'Administración Búnker'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
]
