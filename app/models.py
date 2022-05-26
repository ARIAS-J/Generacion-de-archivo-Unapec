from django.db import models

# Create your models here.
class Nomina(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)
    puesto_trabajo = models.CharField(max_length=50)
    numero_cuenta = models.CharField(max_length=11, unique=True)
    monto_pagar = models.FloatField(max_length=10)
    
    def __str__(self):
        return f"{self.cedula} {self.nombre + self.primer_apellido} {self.puesto_trabajo}"