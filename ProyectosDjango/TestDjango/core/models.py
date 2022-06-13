from django.db import models

# Create your models here.
class Formulario(models.Model):
    Rut = models.IntegerField(primary_key=True, verbose_name='Rut')
    Nombre = models.CharField(max_length=100, verbose_name='Nombre')
    Correo = models.CharField(max_length=100, verbose_name='Correo')
    Telefono = models.IntegerField(verbose_name='Telefono')
    Region = models.CharField(max_length=100, verbose_name='Region')
    Comuna = models.CharField(max_length=100, verbose_name='Comuna')
    
    def __str__(self):
        return self.Rut

class Mascota(models.Model):
    idMascota = models.IntegerField(primary_key=True, verbose_name='idMascota')
    NombreMascota = models.CharField(max_length=100, verbose_name='Nombre Mascota')
    RazaMascota = models.CharField(max_length=50, verbose_name='Raza Mascota')
    EdadMascota = models.IntegerField(verbose_name='Edad Mascota')
    Esterilizacion = models.CharField(max_length=2, verbose_name='Esterilizacion')
    
    def __str__(self):
        return self.NombreMascota

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='idProducto')
    NombreProducto = models.CharField(max_length=200, verbose_name='NombreProducto')
    CategoriaProducto = models.CharField(max_length=200, verbose_name='CategoriaProducto')
    Precio = models.IntegerField(verbose_name='Precio')
    Stock = models.IntegerField(verbose_name='Stock')
    
    def __str__(self):
        return self.idProducto

