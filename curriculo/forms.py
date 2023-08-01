from django import forms
from .models import Educacao, ExperienciaProfissional

class EducacaoForm(forms.ModelForm):
    class Meta:
        model = Educacao
        fields = ['instituicao', 'curso', 'periodo']

class ExperienciaProfissionalForm(forms.ModelForm):
    class Meta:
        model = ExperienciaProfissional
        fields = ['empresa', 'cargo', 'periodo', 'descricao']