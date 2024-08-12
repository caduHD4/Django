from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.forms.widgets import DateTimeInput
from django.urls import reverse_lazy
from .models import Cidade, Pessoa, Carro, Morador, Porteiro, Visita, Apartamento
from django.contrib.auth.mixins import LoginRequiredMixin

class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-cidade')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidade'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar uma nova cidade.'
        context['botao'] = 'Cadastrar Cidade'
        return context

class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-pessoa')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Pessoa'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar uma nova pessoa.'
        context['botao'] = 'Cadastrar Pessoa'
        return context

class CarroCreate(LoginRequiredMixin, CreateView):
    model = Carro
    fields = ['placa', 'modelo', 'cor', 'apartamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-carro')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Carro'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo carro.'
        context['botao'] = 'Cadastrar Carro'
        return context

class MoradorCreate(LoginRequiredMixin, CreateView):
    model = Morador
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'apartamento', 'possui_animais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-morador')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Morador'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo morador.'
        context['botao'] = 'Cadastrar Morador'
        return context

class PorteiroCreate(LoginRequiredMixin, CreateView):
    model = Porteiro
    fields = ['nome', 'turno']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-porteiro')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Porteiro'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo porteiro.'
        context['botao'] = 'Cadastrar Porteiro'
        return context

class VisitaCreate(LoginRequiredMixin, CreateView):
    model = Visita
    fields = ['pessoa_visita', 'pessoa_visitada', 'motivo', 'data_hora_entrada', 'data_hora_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-visita')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Visita'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar uma nova visita.'
        context['botao'] = 'Cadastrar Visita'
        return context

class ApartamentoCreate(LoginRequiredMixin, CreateView):
    model = Apartamento
    fields = ['numero', 'bloco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-apartamento')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Apartamento'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo apartamento.'
        context['botao'] = 'Cadastrar Apartamento'
        return context

##########UPDATE##############

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-cidade')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Cidade'
        context['descricao'] = 'Atualize os campos necessários para modificar a cidade existente.'
        context['botao'] = 'Atualizar Cidade'
        return context

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-pessoa')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Pessoa'
        context['descricao'] = 'Atualize os campos necessários para modificar a pessoa existente.'
        context['botao'] = 'Atualizar Pessoa'
        return context

class CarroUpdate(LoginRequiredMixin, UpdateView):
    model = Carro
    fields = ['placa', 'modelo', 'cor', 'apartamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-carro')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Carro'
        context['descricao'] = 'Atualize os campos necessários para modificar o carro existente.'
        context['botao'] = 'Atualizar Carro'
        return context

class MoradorUpdate(LoginRequiredMixin, UpdateView):
    model = Morador
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'apartamento', 'possui_animais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-morador')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Morador'
        context['descricao'] = 'Atualize os campos necessários para modificar o morador existente.'
        context['botao'] = 'Atualizar Morador'
        return context

class PorteiroUpdate(LoginRequiredMixin, UpdateView):
    model = Porteiro
    fields = ['nome', 'turno']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-porteiro')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Porteiro'
        context['descricao'] = 'Atualize os campos necessários para modificar o porteiro existente.'
        context['botao'] = 'Atualizar Porteiro'
        return context

class VisitaUpdate(LoginRequiredMixin, UpdateView):
    model = Visita
    fields = ['pessoa_visita', 'pessoa_visitada', 'motivo', 'data_hora_entrada', 'data_hora_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-visita')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Visita'
        context['descricao'] = 'Atualize os campos necessários para modificar a visita existente.'
        context['botao'] = 'Atualizar Visita'
        return context

class ApartamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Apartamento
    fields = ['numero', 'bloco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-apartamento')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Apartamento'
        context['descricao'] = 'Atualize os campos necessários para modificar o apartamento existente.'
        context['botao'] = 'Atualizar Apartamento'
        return context

#######DELETE#######

class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-cidade')
    login_url = reverse_lazy('login')

class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-pessoa')
    login_url = reverse_lazy('login')

class CarroDelete(LoginRequiredMixin, DeleteView):
    model = Carro
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-carro')
    login_url = reverse_lazy('login')

class MoradorDelete(LoginRequiredMixin, DeleteView):
    model = Morador
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-morador')
    login_url = reverse_lazy('login')

class PorteiroDelete(LoginRequiredMixin, DeleteView):
    model = Porteiro
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-porteiro')
    login_url = reverse_lazy('login')

class VisitaDelete(LoginRequiredMixin, DeleteView):
    model = Visita
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-visita')
    login_url = reverse_lazy('login')

class ApartamentoDelete(LoginRequiredMixin, DeleteView):
    model = Apartamento
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-apartamento')
    login_url = reverse_lazy('login')

#######LISTA#######

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'
    context_object_name = 'cidades'
    login_url = reverse_lazy('login')

class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'cadastros/listas/pessoa.html'
    context_object_name = 'pessoas'
    login_url = reverse_lazy('login')

class CarroList(LoginRequiredMixin, ListView):
    model = Carro
    template_name = 'cadastros/listas/carro.html'
    context_object_name = 'carros'
    login_url = reverse_lazy('login')

class MoradorList(LoginRequiredMixin, ListView):
    model = Morador
    template_name = 'cadastros/listas/morador.html'
    context_object_name = 'moradores'
    login_url = reverse_lazy('login')

class PorteiroList(LoginRequiredMixin, ListView):
    model = Porteiro
    template_name = 'cadastros/listas/porteiro.html'
    context_object_name = 'porteiros'
    login_url = reverse_lazy('login')

class VisitaList(LoginRequiredMixin, ListView):
    model = Visita
    template_name = 'cadastros/listas/visita.html'
    context_object_name = 'visitas'
    login_url = reverse_lazy('login')

class ApartamentoList(LoginRequiredMixin, ListView):
    model = Apartamento
    template_name = 'cadastros/listas/apartamento.html'
    context_object_name = 'apartamentos'
    login_url = reverse_lazy('login')