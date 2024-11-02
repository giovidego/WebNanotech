"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from .views import VRegistro, cerrar_sesion, iniciar_sesion, lista_usuarios,usuarioAdd,usuarioEdit,usuarioDel

urlpatterns = [
    path('registro', VRegistro.as_view(), name='registro'),
    path('login', iniciar_sesion, name='login'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('usuarios', lista_usuarios, name='usuarios'),
    path('usuarioAdd', usuarioAdd, name='usuarioAdd'),
    path('usuariosEdit/<str:pk>',usuarioEdit, name='usuarioEdit'),
    path('usuarioDel/<str:pk>',usuarioDel, name='usuarioDel'),
    
    
] 

