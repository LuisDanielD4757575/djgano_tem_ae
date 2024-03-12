from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_context = {'Futbol':'Jugar y ver futbol.',
                  'Libros':'Leer libros y mangas.',
                  'Videojuegos':'Jugar videojuegos con mis amigos.'}
    return render(request, 'first/index.html', context=my_context)
    #return HttpResponse("<h1>Cristiano Ronaldo es el mejor de la historia<h1>")
