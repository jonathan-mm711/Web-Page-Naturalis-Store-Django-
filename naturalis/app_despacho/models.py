from django.db import models

# Create your models here.
class Despacho(models.Model):
    numero_despacho=models.CharField(max_length=30)
    nombre_cliente=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    productos=models.CharField(max_length=60)
    peso=models.CharField(max_length=30)
    medidas=models.CharField(max_length=30)
    
    fecha_ingreso=models.CharField(max_length=30)
    fecha_envio=models.CharField(max_length=30)
    estado=models.CharField(max_length=30)
