from django.shortcuts import render

def lista_de_pessoas(request):
    return render(request, 'pessoa.html')

