from django.db import models
from django.contrib.auth import get_user_model
from gestion.models import Producto
from django.db.models import F, Sum, FloatField
# Create your models here.

User=get_user_model()

class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('producto__precio')*F('cantidad'), output_field=FloatField())
        )['total']

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedido'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    
    cantidad = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.cantidad} unidades de {self.producto.nombre} marca {self.producto.marca}'
    
    class Meta:
        db_table='LineaPedidos'
        verbose_name='LineaPedido'
        verbose_name_plural='LineaPedidos'
        ordering = ['id']