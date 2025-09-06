from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Tareas
from django import forms

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
        
def tareas(request):
    tasks = Tareas.objects.all()
    print(tareas)
    return render(request, "tasks.html", {"tareas": tasks})

def tareas_form(request):
    class Tareas_Form(forms.ModelForm):
        """Form definition for Tareas."""
        class Meta:
            """Meta definition for Tareasform."""
            model = Tareas
            fields = ('titulo',"descripcion","importante")
    
    form = Tareas_Form()
    #print(form)
    if request.method == "GET":
        return render(request, "tasks_form.html", {"form":form})
    else:
        #print(request.POST)
        form = Tareas_Form(request.POST)
        #return HttpResponse(request.POST)
        if form.is_valid:
            form.save()
            return redirect(tareas)

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