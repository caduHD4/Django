import django_filters
from django import forms
from .models import Cidade, Pessoa, Carro, Morador, Porteiro, Visita, Apartamento

class CidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Nome da Cidade',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    estado = django_filters.CharFilter(
        lookup_expr='iexact', 
        label='Estado (UF)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'maxlength': '2',
            'placeholder': 'UF'
        })
    )

    class Meta:
        model = Cidade
        fields = ['nome', 'estado']

class PessoaFilter(django_filters.FilterSet):
    nome_completo = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome'
        })
    )
    cpf = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='CPF',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o CPF'
        })
    )
    email = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o email'
        })
    )
    cidade = django_filters.ModelChoiceFilter(
        queryset=Cidade.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'cpf', 'email', 'cidade']

class CarroFilter(django_filters.FilterSet):
    placa = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Placa',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a placa'
        })
    )
    modelo = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Modelo',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o modelo'
        })
    )
    cor = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Cor',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a cor'
        })
    )
    apartamento = django_filters.ModelChoiceFilter(
        queryset=Apartamento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Carro
        fields = ['placa', 'modelo', 'cor', 'apartamento']

class MoradorFilter(django_filters.FilterSet):
    nome_completo = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome'
        })
    )
    cpf = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='CPF',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o CPF'
        })
    )
    apartamento = django_filters.ModelChoiceFilter(
        queryset=Apartamento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    possui_animais = django_filters.BooleanFilter(
        widget=forms.Select(attrs={
            'class': 'form-control'
        }, choices=((None, 'Todos'), (True, 'Sim'), (False, 'Não')))
    )

    class Meta:
        model = Morador
        fields = ['nome_completo', 'cpf', 'apartamento', 'possui_animais']

class PorteiroFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        lookup_expr='icontains', 
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome'
        })
    )
    turno = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Turno',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o turno'
        })
    )

    class Meta:
        model = Porteiro
        fields = ['nome', 'turno']

class VisitaFilter(django_filters.FilterSet):
    data_hora_entrada = django_filters.DateTimeFilter(
        label='Data/Hora Entrada',
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )
    pessoa_visita = django_filters.ModelChoiceFilter(
        queryset=Pessoa.objects.all(),
        label='Visitante',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    pessoa_visitada = django_filters.ModelChoiceFilter(
        queryset=Morador.objects.all(),
        label='Morador Visitado',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Visita
        fields = ['pessoa_visita', 'pessoa_visitada', 'data_hora_entrada']

class ApartamentoFilter(django_filters.FilterSet):
    numero = django_filters.NumberFilter(label='Número')

    class Meta:
        model = Apartamento
        fields = ['numero', 'bloco']