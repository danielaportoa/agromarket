from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0) # Pesos chilenos no usan decimales normalmente
    stock = models.IntegerField(default=0)
    
    es_certificado_organico = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('en_camino', 'En Camino hacia el Campo'),
        ('entregado', 'Entregado'),
    )
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    direccion_envio = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username}"
