from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Tareas
from .forms import Tareas_Form
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required#para proteger rutas

# Create your views here.
def holaMundo(request):
    #return HttpResponse("<h1>hola mundo</h1>")
    title = "Hola mundo"
    #return render(request, "home.html", {"mititulo": title, "form": UserCreationForm})
    return render(request, "helloworld.html", {"mititulo": title})
def inicio(request):
    return render(request, "home.html")

def registro(requets):
    #verificar si el metodo es get o post
    if requets.method =="GET":
        print("metodo get")
        return render(requets, "register.html",{"form": UserCreationForm})
    else:
        #print("metodo POST", requets.POST)
        #return HttpResponse("Enviando datos por metodo post")
        if requets.POST["password1"] == requets.POST["password2"]:
            #mejora utilizar try except
            try:
                user = User.objects.create_user(username=requets.POST["username"],password=requets.POST["password1"])
                user.save()
                login(requets, user)
                #return HttpResponse("Usuario registrado. !!!")
                return redirect(tareas)
            except IntegrityError:
                #return HttpResponse("El usuario ya existe. !!!")
                return render(requets, "register.html", {"form": UserCreationForm, "error": "El usuario ya existe. !!!"})
        else:
            #return HttpResponse("Las contraseñas no son iguales")
            return render(requets, "register.html",{"form": UserCreationForm, "error" : "Las contraseñas no son iguales"})
        
@login_required
def tareas(request):
    #tasks = Tareas.objects.all()
    tasks = Tareas.objects.filter(user=request.user, fecha_completado__isnull=True)#tareas por completar
    #tasks = Tareas.objects.filter(user=request.user)#todas la s tareas
    print(tareas)
    return render(request, "tasks.html", {"tareas": tasks})

@login_required
def tareas_completadas(request):
    tasks = Tareas.objects.filter(user=request.user).order_by("-fecha_completado")#ordena por la fecha
    return render(request, "tasks_completed.html", {"tareas":tasks})

@login_required
def crear_tareas(request):
    #print(form)
    if request.method == "GET":
        return render(request, "tasks_create.html", {"form":Tareas_Form})
    else:
        #print(request.POST)
        form = Tareas_Form(request.POST)
        #devolver los datos que estan en el formulario
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect(tareas)
        # print (new_task)
        # return HttpResponse(request.POST)
        # if form.is_valid:
        #     new_task = form.save(commit=False)
        #     new_task.user = request.user
        #     form.save()#lo guarda en BD
        #     return redirect(tareas)

@login_required
def detalle_tareas(request, id):
    #tarea = Tareas.objects.get(pk=id)#si no encuentra el id, cae el servicio, utiliza get_object_or_404, importarlo en shortcuts
    tarea = get_object_or_404(Tareas, pk=id, user=request.user)#agregar el usuario, para listar solo las tareas de el.
    if request.method == "GET":
        form=Tareas_Form(instance=tarea)#guardamos un formulario con los datos de la tarea de bBD. 
        return render(request, "tasks_details.html", {"tarea": tarea, "form": form})
    else:
        #print(request.POST)#comprobando llegad de datos
        #capturar posible error
        try:
            form = Tareas_Form(request.POST, instance=tarea)
            form.save()
            return redirect("tareas")
        except ValueError:
            return render(request, "tasks_details.html", {"tarea": tarea, "form": form, "erro":"Error actualizando la tarea."})

@login_required
def completada_tareas(request, id):
    tarea = get_object_or_404(Tareas,pk=id,user=request.user)
    if request.method=="POST":
        tarea.fecha_completado = datetime.now()#puede importa timezone de django.utils  timezone
        #tarea.fecha_completado = timezone.now()
        tarea.save()
        return redirect ("tareas")

@login_required
def eliminar_tareas(request, id):
    tarea = get_object_or_404(Tareas, pk=id, user=request.user)
    if request.method=="POST":
        tarea.delete()
        return redirect("tareas")

@login_required
def salir(request):
    logout(request)
    return redirect(inicio)

def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user == None:
            return render(request, "login.html", {"form": AuthenticationForm, "error":"Usuario y/o contraseña incorrectos !!!"})
        else:
            login(request, user)
            return redirect(inicio)