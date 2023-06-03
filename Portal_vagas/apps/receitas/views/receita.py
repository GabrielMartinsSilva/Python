from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from receitas.models import Receita
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    receitas = Receita.objects.order_by('-date').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)


    dados = {"receitas": receitas_por_pagina}

    return render(request, "receitas/index.html", dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {"receita": receita}
    return render(request, "receitas/receita.html", receita_a_exibir)

def cria_receita(request):
    if request.method == 'POST':
        titulo_vaga = request.POST['titulo_vaga']
        localizacao = request.POST['localizacao']
        descricao = request.POST['descricao']        
        salario = request.POST.getlist('salario')                     
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, titulo_vaga=titulo_vaga, localizacao=localizacao, 
        descricao = descricao, salario=salario)       
        receita.save()
        return redirect('dashboard')
    else:  
        return render (request, 'receitas/cria_receita.html')

def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar ={'receita':receita }
    return render(request, 'receitas/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.titulo_vaga = request.POST['titulo_vaga']
        r.localizacao = request.POST['localizacao']
        r.descricao = request.POST['descricao']        
        r.salario = request.POST.getlist('salario[]')
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()    
        return redirect('dashboard')

