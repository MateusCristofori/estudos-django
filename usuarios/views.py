from django.shortcuts import redirect, render


def cadastro(request):
  
  if request.method == 'POST':
    nome = request.POST['nome']
    email = request.POST['email']
    senha = request.POST['password']
    confirmacao_senha = request.POST['password2']    
    print(nome, email, senha, confirmacao_senha)
    return redirect('login')
  else:
    return render(request, 'usuarios/cadastro.html')

def login(request):
  return render(request, 'usuarios/login.html')

def dashboard(request):
  return render(request)

def logout(request):
  return render(request)

