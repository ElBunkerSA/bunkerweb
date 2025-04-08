from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        subcategoria = cleaned_data.get('subcategoria')

        # Definimos las asociaciones válidas entre categoría y subcategoría
        valid_mapping = {
            'perifericos': ['ratones', 'mandos', 'teclados', 'cascos'],
            'videojuegos': ['fisico', 'digital'],
            'hardware': ['consolas', 'pc', 'componentes'],
            'otros': [None, '']
        }

        if categoria in valid_mapping:
            # Para categorías donde la subcategoría debe estar en un listado definido:
            if subcategoria not in valid_mapping[categoria]:
                raise forms.ValidationError(
                    f"La subcategoría seleccionada ('{subcategoria}') no corresponde a la categoría '{categoria}'."
                )
        return cleaned_data
