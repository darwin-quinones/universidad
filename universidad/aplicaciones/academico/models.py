from django.db import models

# Create your models here.
# se crea un modelo con ORM para database
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    # esto es para que muestre el nombre en el admin
    def __str__(self):
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.codigo, self.creditos)

