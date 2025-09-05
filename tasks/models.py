from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tareas (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completado = models.DateTimeField(null=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #ver en el panel el titulo segun los atributos de esta clase.
    def __str__(self):
        #return super().__str__()+self.titulo
        return self.titulo