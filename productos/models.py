from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    costo = models.FloatField(default=0)
    piezas = models.IntegerField(default=0)
    fec_ing = models.DateField(default="2025-01-01")
    categoria = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descuento = models.FloatField(default=0)
    stock_minimo = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.nombre} ({self.marca})"
