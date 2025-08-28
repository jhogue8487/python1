from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def holaMundo(request):
    #return HttpResponse("<h1>hola mundo</h1>")
    title = "Hola mundo"
    #return render(request, "home.html", {"mititulo": title, "form": UserCreationForm})
    return render(request, "home.html", {"mititulo": title})

def login(requets):
    return render(requets, "login.html",{"form": UserCreationForm})