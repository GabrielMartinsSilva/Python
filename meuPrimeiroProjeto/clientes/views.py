from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def lista_de_pessoas(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})



def novas_pessoas(request):
    form = PersonForm(request.POST, request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('lista_de_pessoas')

    return render(request, 'form_pessoas.html', {'form': form})

