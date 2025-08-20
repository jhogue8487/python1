from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    #return HttpResponse("<h1>hola mundo</h1>")
    title = "Hola mundo"
    return render(request, "home.html", {"mititulo": title})