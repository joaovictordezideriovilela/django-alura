from django.shortcuts import render, get_object_or_404
from .models import Receita
# Create your views here.
def index(request):

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    return render(request, 'receita.html', {'receita': receita})

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            lista_receitas = lista_receitas.filter(nome_receita=nome)
    return render(request, 'buscar.html', {'receitas': lista_receitas})