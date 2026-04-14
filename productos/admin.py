from django.contrib import admin
from .models import Categoria, Certificacion, Producto, Pedido, DetallePedido
admin.site.register(DetallePedido)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'es_certificado_organico', 'distancia_km', 'huella_co2')
    list_filter = ('categoria', 'es_certificado_organico', 'kilometro_cero')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('huella_co2',) 
    filter_horizontal = ('certificaciones',)

    def huella_co2(self, obj):
        return f"{obj.huella_carbono_estimada} kg"
    huella_co2.short_description = 'Huella CO2'


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'total_formateado')
    inlines = [DetallePedidoInline]
    readonly_fields = ('total',)

    def total_formateado(self, obj):
        return f"${obj.total}"
    total_formateado.short_description = 'Total'