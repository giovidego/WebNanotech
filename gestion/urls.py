"""
URL configuration for WebNanotech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productosList', views.listaedit, name='productosList'),
    path('productosEdit/<int:pk>',views.productosEdit, name='productosEdit'),
    path('productosDel/<int:pk>',views.productosDel, name='productosDel'),
    path('detalles/<int:pk>',views.detalles, name='detalles'),
    path('ver_pedidos/', views.ver_pedidos, name="ver_pedidos"),
    path('libreta/', views.ver_libreta, name="ver_libreta"),
    path('hojaDel/<int:pk>',views.hojaDel, name='hojaDel'),
    path('hojaEdit/<int:pk>',views.hojaEdit, name='hojaEdit'),
    path('visualizacion',views.analiticas, name='analitica'),
    # path('libretaadd', views.addlibreta, name="libretaadd"),
    path('', views.Bienvenida, name='index'),
    
]


