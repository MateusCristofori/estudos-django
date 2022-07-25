from django.shortcuts import render
from receitas.models import Receita


def buscar(request):
    buscar_receita = Receita.objects.order_by(
        '-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        buscar_receita = buscar_receita.filter(
            nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': buscar_receita
    }
    return render(request, 'receitas/buscar.html', dados)
