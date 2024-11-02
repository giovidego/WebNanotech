from django.db import models

# Create your models here.

class Producto(models.Model):
    sku = models.AutoField(primary_key=True)
    foto= models.ImageField(blank=True, null=True, upload_to='productos')
    nombre= models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(blank=True, null=True, max_length=30)
    detalles = models.CharField(blank=True, null=True, max_length=1000)
    visible = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return "%s, %s %s, stock: %s"% (self.sku ,self.nombre, self.marca, self.cantidad)

#python manage.py makemigrations
#python manage.py sqlmigrate ropa numeromigracion
#python manage.py migrate

# utilidades django sql
    # Agregar usuario
        # python manage.py shell
        # from ropa.models import Usuario
        #
        # usuario = Usuario( usuario='', contrasena='') ----:> crea variable con un objeto Usuario
        # usuario.save()                                ----:> guarda en base de datos variable usuario
        #
        # usuario = Usuario.objects.create(usuario='', contrasena='') ----:> metodo simplificado de lo anterior 
        #
    #
    # Eliminar datos
        # usuario = Usuario.objects.get(id=1) ----:> Obtiene objeto por id
        # usuario.delete()                    ----:> Elimina objeto guardado en variable usuario
        #
    # 
    # Modificar Datos
        # usuario.contrasena=''
        # usuario.save()
        #
    #  
    # Obtener Lista
        # Lista = Usuario.objects.all
        # Lista
        #
    # 
    # Filtro where 
        # Producto.objects.filter(marca='Polemic') 
        # Producto.objects.filter(nombre = 'chaqueta', marca='Polemic') ----:> la coma se utiliza como 'and'
        # Producto.objects.filter(marca='Polemic', precio__lte=29000) ----:> busca precio 'menor e igual que'
        # Producto.objects.filter(marca='Polemic', precio__gte=10000) ----:> busca precio 'mayor e igual que'
        # Producto.objects.filter(marca='Polemic', precio__range=(9000, 31000)) ----:> busca precio 'mayor que' y 'menor que'
    # order by
        # Producto.objects.filter(marca='Polemic', precio__lte=30000).order_by('precio') ----:> ordenar ascendente default
        # Producto.objects.filter(marca='Polemic', precio__lte=30000).order_by('-precio') ----:> ordenar desendente
        #
    # #
