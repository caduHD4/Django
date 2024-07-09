from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Cidade, Pessoa, Carro, Morador, Porteiro, Visita, Apartamento

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

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

##########UPDATE##############

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class CarroUpdate(UpdateView):
    model = Carro
    fields = ['placa', 'modelo', 'cor', 'apartamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class MoradorUpdate(UpdateView):
    model = Morador
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'apartamento', 'possui_animais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class PorteiroUpdate(UpdateView):
    model = Porteiro
    fields = ['nome', 'turno']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class VisitaUpdate(UpdateView):
    model = Visita
    fields = ['pessoa_visita', 'pessoa_visitada', 'motivo', 'data_hora_entrada', 'data_hora_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class ApartamentoUpdate(UpdateView):
    model = Apartamento
    fields = ['numero', 'bloco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

######DELETE######

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

class CarroDelete(DeleteView):
    model = Carro
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

class MoradorDelete(DeleteView):
    model = Morador
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

class PorteiroDelete(DeleteView):
    model = Porteiro
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

class VisitaDelete(DeleteView):
    model = Visita
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

class ApartamentoDelete(DeleteView):
    model = Apartamento
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('inicio')

#######LISTA#######

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'
    context_object_name = 'cidades'

class PessoaList(ListView):
    model = Pessoa
    template_name = 'cadastros/listas/pessoa.html'
    context_object_name = 'pessoas'

class CarroList(ListView):
    model = Carro
    template_name = 'cadastros/listas/carro.html'
    context_object_name = 'carros'

class MoradorList(ListView):
    model = Morador
    template_name = 'cadastros/listas/morador.html'
    context_object_name = 'moradores'

class PorteiroList(ListView):
    model = Porteiro
    template_name = 'cadastros/listas/porteiro.html'
    context_object_name = 'porteiros'

class VisitaList(ListView):
    model = Visita
    template_name = 'cadastros/listas/visita.html'
    context_object_name = 'visitas'

class ApartamentoList(ListView):
    model = Apartamento
    template_name = 'cadastros/listas/apartamento.html'
    context_object_name = 'apartamentos'