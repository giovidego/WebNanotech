from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  . import views



urlpatterns = [
    path('',views.carrito, name='carro'),
    path('agregar/<str:pk>', views.agregar_producto, name="agregar"),

    path('eliminar/<str:pk>', views.eliminar_producto, name="eliminar"),

    path('restar/<str:pk>', views.restar_producto, name="restar"),

    path('sumar/<str:pk>', views.sumar_producto, name="sumar"),

    path('limpiar/', views.limpiar_carroproducto, name="limpiar"),
    
    ]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)