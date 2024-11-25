from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from carro.carro import Carro
from gestion.models import Producto
from pedidos.models import LineaPedido, Pedido

# Create your views here

def is_admin(user):
    return user.is_superuser

@login_required(login_url='login')
@user_passes_test(is_admin)
def mandar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    
    for key, value in carro.carro.items():

        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido


        ))
        cantidad=int(value['cantidad'])
        producto = Producto.objects.get(sku=key)
        producto.cantidad -= cantidad
        producto.save()
    LineaPedido.objects.bulk_create(lineas_pedido)
    carro.limpiar_carro()
    return redirect('index')
