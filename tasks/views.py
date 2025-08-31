from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

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
                user.save
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
    return render(request, "tasks.html")

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