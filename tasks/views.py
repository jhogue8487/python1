from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def holaMundo(request):
    #return HttpResponse("<h1>hola mundo</h1>")
    title = "Hola mundo"
    #return render(request, "home.html", {"mititulo": title, "form": UserCreationForm})
    return render(request, "home.html", {"mititulo": title})

def register(requets):
    #verificar si el metodo es get o post
    if requets.method =="GET":
        print("metodo get")
        return render(requets, "register.html",{"form": UserCreationForm})
    else:
        #print("metodo POST", requets.POST)
        #return HttpResponse("Enviando datos por metodo post")
        if requets.POST["password1"] == requets.POST["password2"]:
            #mejora utilizar catch
            user = User.objects.create_user(username=requets.POST["username"],password=requets.POST["password1"])
            user.save
            return HttpResponse("Usuario registrado. !!!")
        else:
            return HttpResponse("Las contraseñas no son iguales")