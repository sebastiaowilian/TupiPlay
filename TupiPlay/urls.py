from django.contrib import admin
from django.urls import path
from jogadores import views
from jogadores.views import JogadorCreateView
import os
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('jogadores/identifica_jogador', views.identifica_jogador, name="identifica_jogador"),
    path('jogadores/inclui_jogador', views.inclui_jogador, name="inclui_jogador"),
    #path("jogadores/inclui_jogador", JogadorCreateView),
    #path('jogadores/atualiza_jogador/<str:identificador>', views.atualiza_jogador, name="atualiza_jogador"),
]
