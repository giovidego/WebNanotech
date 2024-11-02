from django.contrib import messages
from .carro import Carro
# def importe_total_carro(request):
#     total = 0 
#     if request.user.is_authenticated:
#         for key, value in request.session["carro"].items():
#             total= total +(float(value["precio"])*(value["cantidad"]))
#         else:
#             messages.error(request, "Para ver carrito")
#     return {"importe_total_carro":total}

# def importe_total_carro(request):
#     carro= request.session.get('carro',{})
#     total=0
#     if request.user.is_authenticated:
#         for key, value in request.session["carro"].items(): 
#             total=total+float(value['Precio'])
#     else:
#         messages.error(request, "Para ver carrito")
            
#     return {'importe_total_carro':total} 

def importe_total_carro(request):
    total = 0
    if 'carro' in request.session:
        carro = request.session['carro']
        for value in carro.values():
            cantidad = int(value.get('cantidad'))
            precio = int(value.get('precio'))
            total += precio * cantidad

    return {'importe_total_carro': total}
