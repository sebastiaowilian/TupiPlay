# Generated by Django 5.0.4 on 2024-05-16 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0001_initial'),
        ('jogos', '0006_partida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partidas_Resumo',
            fields=[
                ('id_partida_resumo', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id partidas resumo')),
                ('qt_pontos', models.IntegerField(default=0, verbose_name='Pontuação')),
                ('qt_acerto', models.IntegerField(default=0, verbose_name='Acertos')),
                ('qt_erro', models.IntegerField(default=0, verbose_name='Erros')),
                ('qt_continuar', models.IntegerField(default=0, verbose_name='Continuações')),
                ('qt_duracao_minutos', models.IntegerField(default=0, verbose_name='Duração')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
                ('id_idioma_1', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='partidas_resumo_idioma_1', to='jogadores.idioma', verbose_name='Idioma nativo')),
                ('id_idioma_2', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='partidas_idioma_2', to='jogadores.idioma', verbose_name='Idioma aprendizado')),
                ('id_jogador', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogadores.jogador', verbose_name='Jogador(a)')),
                ('id_jogo', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogos.jogo', verbose_name='Jogo escolhido')),
            ],
        ),
    ]
