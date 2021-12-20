"""naturalis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app_despacho import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.Index),
    path('ingresar_despacho/',views.Ingresar_despacho),
    path('ingreso_despacho/',views.ingreso_despacho),
    path('listar_todo/',views.listar_todo),
    path('Listar_todo/',views.Listar_todo),
    path('eliminar_despacho/',views.Eliminar_despachos),
    path('eliminacion_despacho/',views.eliminacion_despacho),
    path('busqueda_despacho/',views.busqueda_despachos),
    path('buscar/',views.buscar),
    path('confirmar_despacho/',views.Confirmar_despachos),
    path('confirmar/',views.confirmar),
    path('listar_entregado/',views.listar_entregado),
    path('listar_por_entregar/',views.listar_por_entregar),
]
