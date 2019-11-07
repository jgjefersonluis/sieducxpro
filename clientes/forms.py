from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'telefone', 'responsavel', 'pesquisador']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Informe o nome do cliente'}),
            'idade': forms.TextInput(attrs={'placeholder': 'Informe a idade do cliente'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Informe o telefone'}),
            'resposavel': forms.TextInput(attrs={'placeholder': 'Informe o nome de resposavel'}),
            'pesquisador': forms.TextInput(attrs={'placeholder': 'Informe o nome do pesquisador'}),

        }