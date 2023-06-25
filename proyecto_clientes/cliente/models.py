from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(max_length=15)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return """Identificacion: %s\n
                Nombres: %s\n
                Apellidos: %s\n
                correo: %s\n
                Edad: %d""" % (self.identificacion, self.nombres,
                self.apellidos,
                self.correo,
                self.edad)
