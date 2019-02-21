from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse('O ano digitado foi ' + str(year))


def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Gabriel', 'idade': 23},
        {'nome': 'Ana', 'idade': 28},
        {'nome': 'Tiribim', 'idade': 29}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
