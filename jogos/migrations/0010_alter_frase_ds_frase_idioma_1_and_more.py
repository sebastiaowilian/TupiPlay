# Generated by Django 5.0.4 on 2024-05-16 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0009_alter_frase_ds_frase_idioma_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frase',
            name='ds_frase_idioma_1',
            field=models.CharField(max_length=300, unique=True, verbose_name='Frase idioma nativo'),
        ),
        migrations.AlterField(
            model_name='frase',
            name='ds_frase_idioma_2',
            field=models.CharField(max_length=300, verbose_name='Frase idioma aprendizado'),
        ),
    ]
