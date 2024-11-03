from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from gestion.models import Producto
from pedidos.models import LineaPedido, Pedido


def is_admin(user):
    return user.is_superuser


@login_required(login_url='login')
@user_passes_test(is_admin)
def productosAdd(request):
    context ={}
    
    if request.method == "POST":
        opcion = request.POST["opcion"]
        print(opcion)
        
        if opcion == "Añadir Producto":
            print("Opcion: "+opcion)
            try:
                if request.POST["sku"] == "":
                    last_sku = Producto.objects.all().order_by('sku').last()
                    sku = last_sku.sku + 1 if last_sku else 1
                    try:
                        foto = request.FILES["fotop"]
                    except:
                        foto = 'productos/fotodefault.png'
                    nombre= request.POST["nombrep"]
                    marca = request.POST["marcap"]
                    cantidad = int(request.POST["cantidadp"])
                    precio = int(request.POST["preciop"])
                    descripcion = request.POST["descripcionp"]
                    detalles = request.POST["detallesp"]
            
                    print(sku, nombre, marca, cantidad, precio)

                    producto = Producto.objects.create(sku=sku, foto=foto, nombre=nombre, marca=marca, cantidad=cantidad, precio=precio, descripcion=descripcion, detalles=detalles)
                    print(producto.foto)
                    producto.save()
                    context={'ac':'El producto ha sido agregado correctamente'}
                    return render(request, 'productosAdd.html', context)
                else:
                    sku = request.POST["sku"]
                    try:
                        foto = request.FILES["fotop"]
                    except:
                        foto = 'productos/fotodefault.png'
                    nombre= request.POST["nombrep"]
                    marca = request.POST["marcap"]
                    cantidad = int(request.POST["cantidadp"])
                    precio = int(request.POST["preciop"])
                    descripcion = request.POST["descripcionp"]
                    detalles = request.POST["detallesp"]
            
                    print(sku, nombre, marca, cantidad, precio)

                    producto = Producto.objects.create(sku=sku, foto=foto, nombre=nombre, marca=marca, cantidad=cantidad, precio=precio, descripcion=descripcion, detalles=detalles)
                    print(producto.foto)
                    producto.save()
                    context={'ac':'El producto ha sido agregado correctamente'}
                    return render(request, 'productosAdd.html', context)
                        
            except:
                
                context={'ac2':'No se pudo agregar el producto SKU(id) ya existe'}
                return render(request, 'productosAdd.html', context)
        
        if opcion == "Editar":
            return redirect('productosList')
        
        if opcion == "Actualizar":
            print("Entró a actualizar")
            print("Opción="+opcion)
            sku = request.POST["sku"]
            if "fotop" in request.FILES:
                foto = request.FILES["fotop"]
            else:
                producto = Producto.objects.get(sku=sku)  
                foto = producto.foto 
            nombre= request.POST["nombrep"]
            marca = request.POST["marcap"]
            cantidad = int(request.POST["cantidadp"])
            precio = int(request.POST["preciop"])
            descripcion = request.POST["descripcionp"]
            detalles = request.POST["detallesp"]

            producto = Producto.objects.get(sku=sku)
            producto.sku=sku
            producto.foto=foto
            producto.nombre=nombre
            producto.marca=marca
            producto.cantidad=cantidad
            producto.precio=precio
            producto.descripcion=descripcion
            producto.detalles=detalles
            producto.save()

        
            productos = Producto.objects.all() 
            context={"productos": productos,"ac":"Bien, datos actualizados"}

            return render(request,'productosList.html',context)
        
    return render(request, 'productosAdd.html', context)

@login_required(login_url='login')
@user_passes_test(is_admin)
def productosEdit(request,pk):
    print("Hola estoy en productosEdit", pk)
    context={}
    producto = Producto.objects.get(sku=pk)
               
    context={"producto":producto}
    
    print("salió del for")
    return render(request,'productosEdit.html',context)

@login_required(login_url='login')
@user_passes_test(is_admin)
def productosDel(request, pk):
    print("Hola estoy en productosDel")
    try:
        producto = Producto.objects.get(sku=pk)
        nom= producto.nombre
        ruta_foto="media/"+str(producto.foto)
        producto.delete()
        if ruta_foto != "media/productos/fotodefault.png":
            import os
            os.remove(ruta_foto)

        productos = Producto.objects.all().values()
        context = {'ac':'Producto ('+str(nom)+') eliminado correctamente',"productos": productos}
        return redirect('productosList')
    except:
        productos = Producto.objects.all()  
        context = {'ac':'No se pudo eliminar producto ('+str(nom)+')', "productos": productos}
        return render(request,'productosList.html', context)

@login_required(login_url='login')
@user_passes_test(is_admin)
def ver_pedidos(request):   
    pedidos = Pedido.objects.all()
    lineas_pedidos = LineaPedido.objects.filter(pedido__in=pedidos)
    context = {"pedidos": pedidos, "lineas_pedidos": lineas_pedidos}
    return render(request, 'verpedidos.html', context)



def Bienvenida(request):
    productos = Producto.objects.all().values()
    context = {"productos": productos}
    return render(request,'bienvenida.html', context)

def listaedit(request):
    productos = Producto.objects.all().values()
    context = {"productos": productos}
    return render(request, 'productosList.html', context)

def detalles(request, pk):
    print("Hola estoy en detalles producto", pk)
    context={}
    producto = Producto.objects.get(sku=pk)
    context={"producto":producto}
    print("salió del for")
    return render(request,'detalleproducto.html',context)

# def carro(request):
#     context={"carro":carro}
#     return render(request, "carro.html",context)












