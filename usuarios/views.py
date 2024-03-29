from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        confirmacao_senha = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, "O nome não pode ficar em branco")
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, "O email não pode ficar em branco")
            return redirect('cadastro')
        if verificacao_senha(senha, confirmacao_senha):
            messages.error(request, 'As senhas não são iguais.')
            print('As senhas precisam ser iguais!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exits():
            messages.error(
                request, 'Nome de usuário já cadastrado. Tente outro nome.')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado.')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(
                request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')


def dashboard(request):

    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        paginator = Paginator(receitas, 3)
        page = request.GET.get('page')
        receitas_por_pagina = paginator.get_page(page)

        dados = {
            'receitas': receitas_por_pagina
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def campo_vazio(campo):
    return not campo.strip()


def verificacao_senha(senha1, senha2):
    return senha1 != senha2
