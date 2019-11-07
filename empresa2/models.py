from django.db import models

# Create your models here.

class registro(models.Model):
	id_registro=models.AutoField(primary_key = True)
	id_cliente =  models.AutoField(primary_key = True)
	nombres = models.CharField(max_length = 120)
	apellidos = models.CharField(max_length = 120)
	contraseña= models.CharField(max_length = 120)
	id_tipo=models.Charfield(max_length=1)
	nroCuenta=models.CharField(max_length=10)
	def __str__(self):
		return self.nombres+' '+self.apellidos
