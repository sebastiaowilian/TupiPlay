from django.forms import ModelForm
from django import forms
from .models import Jogador, Idioma, Escolaridade

class FormJogador(ModelForm):
    class Meta:
        model = Jogador        
        exclude = ['dt_inclusao', 'id_usuario_inclusao','dt_alteracao', 'id_usuario_alteracao','dt_exclusao', 'id_usuario_exclusao']
    
    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:            
            self.fields[field].widget.attrs.update({'placeholder': field})
            
            
        choices = list()
        for i, j in self.fields['Choices_Tipo_Genero'].choices:
            tp_genero = CategoriaManutencao.objects.get(tp_genero=j)
            choices.append((i.value, categoria.get_titulo_display()))
        
        self.fields['Choices_Tipo_Genero'].choices = choices'''