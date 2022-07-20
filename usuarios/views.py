from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita


def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        confirmacao_senha = request.POST['password2']
        print(nome, email, senha, confirmacao_senha)
        if not nome.strip():
            print("O nome não pode ficar em branco")
            return redirect('cadastro')
        if not email.strip():
            print("O email não pode ficar em branco")
            return redirect('cadastro')
        if senha != confirmacao_senha:
            print('As senhas precisam ser iguais!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado.')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
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

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cria_receita(request):

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes,
                                         modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')
