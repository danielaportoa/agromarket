from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    # Esto incluirá la información de la categoría dentro del producto
    categoria_info = CategoriaSerializer(source='categoria', read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'imagen', 'descripcion', 'precio', 'certificado_organico', 'stock', 'categoria']
