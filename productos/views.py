from rest_framework import viewsets
from .models import Producto, Categoria, Pedido, DetallePedido
from .serializers import ProductoSerializer, CategoriaSerializer
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})

@csrf_exempt
def finalizar_compra(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            carrito = data.get('carrito')
            total = data.get('total')

            usuario_pedido = request.user if request.user.is_authenticated else User.objects.first()

            pedido = Pedido.objects.create(
                usuario=usuario_pedido, 
                total=total
            )

            for item in carrito:
                producto = Producto.objects.get(id=item['id'])
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=item['cantidad'],
                    precio_unitario=item['precio']
                )

            return JsonResponse({'status': 'success', 'pedido_id': pedido.id}, status=201)
        
        except Exception as e:

            print(f"ERROR EN COMPRA: {e}")
            return JsonResponse({'error': str(e)}, status=400)