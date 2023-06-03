from .receita import *
from .busca import *
from django.shortcuts import get_object_or_404, render, redirect
from receitas.models import Receita

def busca(request):
    lista_receitas = Receita.objects.order_by('-date').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(titulo_vaga__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }        

    return render(request, 'receitas/buscar.html', dados)    