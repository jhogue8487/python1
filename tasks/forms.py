from django.forms import ModelForm
from .models import Tareas

class Tareas_Form(ModelForm):
        """Form definition for Tareas."""
        class Meta:
            """Meta definition for Tareasform."""
            model = Tareas
            fields = ('titulo',"descripcion","importante")