from django.shortcuts import render
from app_despacho.models import Despacho
from django.http import HttpResponse
import time
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import Http404


def Index(request):
    return render(request,"index.html")

def Ingresar_despacho(request):
    return render(request,"ingresar_despacho.html")

def Listar_todo(request):
    return render(request,"listar_todo.html")

def Eliminar_despachos(request):
    return render(request,"eliminar_despacho.html")

def busqueda_despachos(request):
    return render(request,"busqueda_despacho.html")

def Confirmar_despachos(request):
    return render(request,"confirmar_despacho.html")

# Create your views here.
def listar_por_entregar(request):
    datos = Despacho.objects.filter(estado="por enviar")
    
    #si no existe la pagina muestre la 1
    page = request.GET.get('page',1)
    try:
        #muestra 5 registros por pagina
        paginator = Paginator(datos,5)
        #la presenta
        datos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity':datos,
        'paginator':paginator
    }
    return render(request,"listar_todo.html",data)

def listar_entregado(request):
    datos = Despacho.objects.filter(estado="entregado")
    
    #si no existe la pagina muestre la 1
    page = request.GET.get('page',1)
    try:
        #muestra 5 registros por pagina
        paginator = Paginator(datos,5)
        #la presenta
        datos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity':datos,
        'paginator':paginator
    }
    return render(request,"listar_todo.html",data)

def listar_todo(request):
    datos = Despacho.objects.all()
    #si no existe la pagina muestre la 1
    page = request.GET.get('page',1)
    try:
        #muestra 5 registros por pagina
        paginator = Paginator(datos,5)
        #la presenta
        datos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity':datos,
        'paginator':paginator
    }
    return render(request,"listar_todo.html",data)

def ingreso_despacho(request):
    numero_despacho = request.GET["txt_numero_despacho"]
    nombre_cliente = request.GET["txt_nombre_cliente"]
    direccion = request.GET["txt_direccion"]
    telefono = request.GET["txt_telefono"]
    productos = request.GET["opt_producto"]
    peso = request.GET["txt_peso"]
    medidas = request.GET["txt_medidas"]
    fecha_ingreso = (time.strftime("%d/%m/%y"))
    estado = "por enviar"

    if len(numero_despacho)>0 and len(nombre_cliente)>0 and len(direccion)>0 and len(telefono)>0 and len(productos)>0 and len(peso)>0 and len(medidas)>0:  
        des = Despacho(numero_despacho=numero_despacho,nombre_cliente=nombre_cliente,direccion=direccion,telefono=telefono,productos=productos,peso=peso,medidas=medidas,fecha_ingreso=fecha_ingreso,estado=estado)
        des.save()
        mensaje =messages.success(request,'Se ha ingresado el despacho')
        mensaje = "Despacho Ingresado"
    else:
         mensaje = "Despacho NO Ingresado , Faltan Datos"
    return HttpResponse(mensaje)


def eliminacion_despacho(request):
    if request.GET["txt_numero_despacho"]:
        numero_recibido = request.GET["txt_numero_despacho"]
        despacho = Despacho.objects.filter(numero_despacho=numero_recibido)
        if despacho:
            des = Despacho.objects.get(numero_despacho=numero_recibido)
            des.delete()
            mensaje = "Despacho Eliminado"
        else:
            mensaje = "Despacho NO Eliminado ... No existe producto con ese numero"
    else:
        mensaje = "Debe ingresar un numero para eliminar"
    return HttpResponse(mensaje)
        
def buscar(request):
    if request.GET["txt_numero_despacho"]:
        despacho = request.GET["txt_numero_despacho"]
        despachos = Despacho.objects.filter(numero_despacho=despacho)
        return render(request,"listar.html",{"despachos":despachos,"query":despacho})
    else:
        mensaje = "Debe ingresar un numero de despacho"
    return HttpResponse(mensaje)

def confirmar(request):
    if  request.GET["txt_numero_despacho"]:
        numero_recibido = request.GET["txt_numero_despacho"]
        despacho = Despacho.objects.filter(numero_despacho=numero_recibido)
        if despacho:
            fecha_envio = (time.strftime("%d/%m/%y"))
            estado = "entregado"
            des = Despacho.objects.get(numero_despacho=numero_recibido)
            des.fecha_envio=fecha_envio
            des.estado=estado
            des.save()
            mensaje = "Despacho Confirmado"
        else:
            mensaje = "No existe despacho para confirmar"
    else:
        mensaje = "Debe ingresar un numero para confirmar"
    return HttpResponse(mensaje)