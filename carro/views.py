from django.shortcuts import render, redirect
from .carro import Carro
from gestion.models import Producto
from django.contrib.auth.decorators import login_required
# Create your views here.

def carrito(request):
    context={"carro":carrito}
    return render(request, "carro.html",context)

@login_required(login_url='login')
def agregar_producto(request, pk):
    # if request.method == 'POST':
    #     carro = Carro(request)
    #     cantidad_producto = request.POST.get('cantidad_p')
        
    #     producto = Producto.objects.get(sku=pk)

    #     carro.agregar(producto,cantidad_producto)
    
    #     return redirect("index")
    if request.method == 'POST':
        carro = Carro(request)
        cantidad_producto = int(request.POST.get('cantidad_p', 1))  # Establece una cantidad predeterminada de 1 si no se envía cantidad
        
        producto = Producto.objects.get(sku=pk)
        
        # Comprueba si el producto ya está en el carrito
        if carro.existe(producto):
            # Actualiza la cantidad del producto en el carrito
            carro.actualizar(producto, cantidad_producto)
        else:
            # Agrega el producto al carrito si no existe
            carro.agregar(producto, cantidad_producto)
    
        return redirect("index")

@login_required(login_url='login')
def eliminar_producto(request,pk):
    carro= Carro(request)
    producto= Producto.objects.get(sku=pk)

    carro.eliminar(producto)
    
    return redirect("carro")

@login_required(login_url='login')
def sumar_producto(request,pk):
    carro= Carro(request)
    producto= Producto.objects.get(sku=pk)

    carro.sumar_producto(producto=producto)
    
    return redirect("carro")

@login_required(login_url='login')
def restar_producto(request,pk):
    carro= Carro(request)
    producto= Producto.objects.get(sku=pk)

    carro.restar_producto(producto=producto)
    
    return redirect("carro")

@login_required(login_url='login')
def limpiar_carroproducto(request):
    carro= Carro(request)
    carro.limpiar_carro()
    
    return redirect("carro")

