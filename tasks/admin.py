from django.contrib import admin

from tasks.models import Tareas

class TareasAdmin(admin.ModelAdmin):
    readonly_fields= ("fecha_creacion",)

# Register your models here.
admin.site.register(Tareas, TareasAdmin)
