from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DetallePedido

@receiver(post_save, sender=DetallePedido)
def actualizar_stock(sender, instance, created, **kwargs):
    if created: # Solo si es un registro nuevo
        producto = instance.producto
        producto.stock -= instance.cantidad
        producto.save()