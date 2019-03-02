from django.shortcuts import render
from .models import Person

def lista_de_pessoas(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

