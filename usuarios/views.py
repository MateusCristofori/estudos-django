from unicodedata import name
from django.shortcuts import render


def cadastro(request):
  return render(request, 'usuarios/cadastro.html')

def login(request):
  return render(request, 'usuarios/login.html')

def dashboard(request):
  return render(request)

def logout(request):
  return render(request)

