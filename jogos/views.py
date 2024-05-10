
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    # Acessa informações da sessão
    print('Sebastiao')
    print(request.session)
    id = request.session.get('id_jogador', 'None') #'1' #request.session['id_jogador']
    avatar =  request.session.get('nm_avatar','None')
    nome =  request.session.get('nm_jogador', 'None')

    # Passa os valores para o contexto
    context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome}
    return render(request, 'home.html', context)


def jogo_quiz(request):
    return render(request, 'jogo_quiz.html')