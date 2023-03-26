from django.db import models

# Create your models here.
class UsuarioNuevo(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)
    correo  = models.IntegerField()
    telefono  = models.IntegerField()
    email = models.EmailField(max_length=254)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nombre
    
