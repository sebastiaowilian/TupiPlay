# Generated by Django 5.0.4 on 2024-05-10 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jogadores', '0004_alter_escolaridade_dt_alteracao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id_jogo', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='ID jogo')),
                ('nm_jogo', models.CharField(max_length=30, unique=True, verbose_name='Nome jogo')),
                ('ds_jogo', models.CharField(max_length=100, null=True, verbose_name='Descrição jogo')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_Dificuldade',
            fields=[
                ('id_nivel_dificuldade', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id nível dificuldade')),
                ('nm_nivel_dificuldade', models.CharField(max_length=30, unique=True, verbose_name='Nome nível dificuldade')),
                ('ds_nivel_dificuldade', models.CharField(max_length=100, null=True, verbose_name='Descrição dificuldade')),
                ('vl_nivel_dificuldade', models.IntegerField(default=0, null=True, verbose_name='Valor nível dificuldade')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_Jogador',
            fields=[
                ('id_nivel_jogador', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id nível jogador')),
                ('nm_nivel_jogador', models.CharField(max_length=30, unique=True, verbose_name='Nome nível jogador')),
                ('ds_nivel_jogador', models.CharField(max_length=100, null=True, verbose_name='Descrição nível jogador')),
                ('vl_nivel_jogador', models.IntegerField(default=0, null=True, verbose_name='Valor nível jogador')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
            ],
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id_frase', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id frase')),
                ('ds_frase_idioma_1', models.CharField(max_length=100, unique=True, verbose_name='Frase idioma nativo')),
                ('ds_frase_idioma_2', models.CharField(max_length=100, verbose_name='Frase idioma aprendizado')),
                ('nm_arquivo_imagem', models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de imagem')),
                ('nm_arquivo_som', models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de som')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
                ('id_idioma_1', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='frases_idioma_1', to='jogadores.idioma', verbose_name='Idioma nativo')),
                ('id_idioma_2', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='frases_idioma_2', to='jogadores.idioma', verbose_name='Idioma aprendizado')),
            ],
        ),
        migrations.CreateModel(
            name='Motivacional',
            fields=[
                ('id_motivacao', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id Idioma')),
                ('msg_motivacional', models.CharField(max_length=30, unique=True, verbose_name='Mensagem motivacional')),
                ('tp_motivacional', models.CharField(choices=[('A', 'Após Acerto'), ('E', 'Após Erro')], max_length=1, verbose_name='Tipo motivação')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
                ('id_idioma', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogadores.idioma', verbose_name='Idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id_partida', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id partida')),
                ('tp_recurso', models.CharField(choices=[('E', 'Escrita'), ('I', 'Imagem'), ('S', 'Som')], max_length=1, verbose_name='Tipo recurso')),
                ('qt_pontos', models.IntegerField(default=0, verbose_name='Pontuação')),
                ('qt_acerto', models.IntegerField(default=0, verbose_name='Acertos')),
                ('qt_erro', models.IntegerField(default=0, verbose_name='Erros')),
                ('qt_continuar', models.IntegerField(default=0, verbose_name='Continuações')),
                ('dt_inicio_partida', models.DateTimeField(blank=True, null=True, verbose_name='Início')),
                ('qt_duracao_minutos', models.IntegerField(default=0, verbose_name='Duração')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
                ('id_idioma_1', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='partida_idioma_1', to='jogadores.idioma', verbose_name='Idioma nativo')),
                ('id_idioma_2', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='partida_idioma_2', to='jogadores.idioma', verbose_name='Idioma aprendizado')),
                ('id_jogo', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogos.jogo', verbose_name='Jogo escolhido')),
            ],
        ),
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
                ('id_jogo', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='jogos.jogo', verbose_name='Jogo escolhido')),
            ],
        ),
        migrations.CreateModel(
            name='Verbete',
            fields=[
                ('id_verbete', models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Id verbete')),
                ('nm_verbete_idioma_2', models.CharField(max_length=100, unique=True, verbose_name='Verbete idioma aprendizado')),
                ('ds_verbete_idioma_1', models.CharField(max_length=100, verbose_name='Definição verbete idioma nativo')),
                ('nm_arquivo_imagem', models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de imagem')),
                ('nm_arquivo_som', models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de som')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')),
                ('id_usuario_inclusao', models.IntegerField(default=0, verbose_name='Usuário inclusao')),
                ('dt_alteracao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data alteração')),
                ('id_usuario_alteracao', models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')),
                ('dt_exclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão')),
                ('id_usuario_exclusao', models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')),
                ('id_idioma_1', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='verbete_idioma_1', to='jogadores.idioma', verbose_name='Idioma nativo')),
                ('id_idioma_2', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='verbete_idioma_2', to='jogadores.idioma', verbose_name='Idioma aprendizado')),
            ],
        ),
    ]
