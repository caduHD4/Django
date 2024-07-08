from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Cidade, Pessoa, Carro, Morador, Porteiro, Visita, Apartamento

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class CarroCreate(CreateView):
    model = Carro
    fields = ['placa', 'modelo', 'cor', 'apartamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class MoradorCreate(CreateView):
    model = Morador
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'apartamento', 'possui_animais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class PorteiroCreate(CreateView):
    model = Porteiro
    fields = ['nome', 'turno']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class VisitaCreate(CreateView):
    model = Visita
    fields = ['pessoa_visita', 'pessoa_visitada', 'motivo', 'data_hora_entrada', 'data_hora_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class ApartamentoCreate(CreateView):
    model = Apartamento
    fields = ['numero', 'bloco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')
