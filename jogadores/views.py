from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
#import os
# Importação de código criados por nós
from .models import Jogador
from .forms import FormJogador

#diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
#caminho_template = os.path.join(diretorio_raiz, 'templates', 'home.html')
# Definição das CBVs: Class Based Views
class JogadorCreateView(CreateView): 
    model = Jogador
    fields = ["nm_joador","nm_avatar","nm_arquivo_imagem","dt_nascimento","cd_cep","nm_email","nm_senha","dt_inclusao","id_escolaridade_id","tp_genero","id_idioma_id"]
    sucess_url = reverse_lazy("identifica_jogador")


# Create your views here.
def home(request):
    return render(request, 'home.html')

def identifica_jogador(request):
    if request.method == "GET":
        #form = FormJogador()
        #return render(request, 'inclui_jogador.html', {'form':form})
        return render(request, "identifica_jogador.html")
    elif request.method== "POST":
        form = FormJogador(request.POST)
        if form.is_valid():            
            request.session['id_jogador'] = '1'
            request.session['nm_avatar'] = 'Sebah'
            request.session['nm_jogador'] = 'Sebastião Wilian da Silva Cardoso'

            #form.save()
            #return HttpResponse('Salvo com sucesso')
            return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'identifica_jogador.html', {'form': form})    
    
    

def inclui_jogador(request):
    if request.method == "GET":
        form = FormJogador()
        return render(request, 'inclui_jogador.html', {'form':form})
    elif request.method== "POST":
        form = FormJogador(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('Salvo com sucesso')
            return render(request, 'identifica_jogador.html', {'form': form})
        else:
            return render(request, 'inclui_jogador.html', {'form': form})
        