from rest_framework import serializers
from .models import Producto, Categoria, Certificacion

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']

class CertificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacion
        fields = ['id', 'nombre', 'descripcion', 'icono']

class ProductoSerializer(serializers.ModelSerializer):
    # Traemos los detalles de la categoría y certificaciones en lugar de solo el ID
    categoria = CategoriaSerializer(read_only=True)
    certificaciones = CertificacionSerializer(many=True, read_only=True)
    
    # Exponemos la propiedad calculada de la huella de carbono
    huella_carbono_estimada = serializers.ReadOnlyField()

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen',
            'categoria', 'certificaciones', 'es_certificado_organico',
            'kilometro_cero', 'distancia_km', 'huella_carbono_estimada',
            'fecha_creacion'
        ]