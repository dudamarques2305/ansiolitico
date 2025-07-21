from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['usuario']

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = InstituicaoApoio
        fields = '__all__'

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoAnsiedade
        fields = '__all__'

class AutoAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = AutoAvaliacao
        fields = '__all__'

class AlertaForm(forms.ModelForm):
    class Meta:
        model = Alerta
        fields = '__all__'

class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = '__all__'
