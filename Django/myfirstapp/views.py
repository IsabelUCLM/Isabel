from django.shortcuts import render
from django.http import HttpResponse #Línea importada por mí

# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola</h1>")

def acercade(request):
    return HttpResponse("Sobre mí")