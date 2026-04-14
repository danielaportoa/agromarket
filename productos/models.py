from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Certificacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    icono = models.ImageField(upload_to='certificaciones/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0) # Ideal para CLP
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    # Atributos de Sustentabilidad
    es_certificado_organico = models.BooleanField(default=False)
    certificaciones = models.ManyToManyField(Certificacion, blank=True)
    kilometro_cero = models.BooleanField(default=False)
    distancia_km = models.PositiveIntegerField(
        default=0, 
        help_text="Distancia desde el origen al centro de distribución en km"
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def huella_carbono_estimada(self):
        factor_emision = 0.12 
        return round(self.distancia_km * factor_emision, 2)

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
    pagado = models.BooleanField(default=False)

    def actualizar_total(self):
        total_calculado = sum(item.cantidad * item.precio_unitario for item in self.detalles.all())
        self.total = total_calculado
        self.save()

    def __str__(self):
        username = self.cliente.username if self.cliente else "Anónimo"
        return f"Pedido #{self.id} - {username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.producto.stock -= self.cantidad
            self.producto.save()
        
        super().save(*args, **kwargs)
        
        self.pedido.actualizar_total()

    def save(self, *args, **kwargs):
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        
        if not self.pk:
            self.producto.stock -= self.cantidad
            self.producto.save()
            
        super().save(*args, **kwargs)
        self.pedido.actualizar_total()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
