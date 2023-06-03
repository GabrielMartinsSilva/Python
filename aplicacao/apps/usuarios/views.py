from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from receitas.models import Receita
from .schemas import CreateUserSchema
from marshmallow import ValidationError


def cadastro(request):
    """ Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        print(request.POST)
        schema = CreateUserSchema()
        data = {
            'nome': request.POST['nome'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'password2': request.POST['password2']
        }

        try:
            data = schema.load(data)
        except ValidationError as err:
            messages.error(request, str(err))
            return redirect('cadastro')
    
        # if campo_vazio(nome):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cadastro')
        # if campo_vazio(email):
        #     messages.error(request, 'O campo email não pode ficar em branco')
        #     return redirect('cadastro')    
        # if senhas_nao_sao_iguais(senha, senha2):
        #     messages.error(request, 'As senhas não são iguais')
        #     print('As senhas não são iguais')
        #     return redirect('cadastro')  
        if User.objects.filter(email=data['email']).exists():
            messages.error (request, 'Usuário já cadastrado')
            return redirect('cadastro') 
        if User.objects.filter(username=data['nome']).exists():
            messages.error (request, 'Usuário já cadastrado')
            return redirect('cadastro')      
        user = User.objects.create_user(username=data['nome'], email=data['email'], password = data['password'])   
        user.save()        
        messages.success(request, 'Cadastro realizado com sucesso')      
        return redirect ('login')
    else:
     return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de uma pessoa no sistema """
    if request.method == 'POST':              
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email ou senha estão em branco')
            return redirect('login')      
        #breakpoint()                
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)            
            if user:
                auth.login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha invalidos !')
            return redirect('login')

            
    return render(request, 'usuarios/login.html')

def logout(request):
    """ Desloga o usuário """
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """ Verifica se o usuário esta logado e mostra o dashboard """
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return  render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index') 
       
def campo_vazio(campo):
    """ Função para verificar um campo vazio """
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    """ Validar se o confirmar senha ao cadastrar está igual a senha original """
    return senha != senha2

