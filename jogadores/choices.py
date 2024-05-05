from django.db.models import TextChoices
from django.utils.translation import gettext as _

class Choices_Tipo_Genero(TextChoices):
    MASCULINO = "M", "Masculino"
    FEMININO = "F", "Feminino"
    NAOINFORMADO = "N", "Não informado"