<<<<<<< HEAD
from django.contrib import messages
from .carro import Carro


def importe_total_carro(request):
    total = 0
    if 'carro' in request.session:
        carro = request.session['carro']
        for value in carro.values():
            cantidad = int(value.get('cantidad'))
            precio = int(value.get('precio'))
            total += precio * cantidad

    return {'importe_total_carro': total}
=======
from django.contrib import messages
from .carro import Carro


def importe_total_carro(request):
    total = 0
    if 'carro' in request.session:
        carro = request.session['carro']
        for value in carro.values():
            cantidad = int(value.get('cantidad'))
            precio = int(value.get('precio'))
            total += precio * cantidad

    return {'importe_total_carro': total}
>>>>>>> 77b3203bc8f619758b59b020ded599290df4236a
