from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.forms.widgets import DateTimeInput
from django.urls import reverse_lazy
from .models import Cidade, Pessoa, Carro, Morador, Porteiro, Visita, Apartamento
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin # type: ignore

from django_filters.views import FilterView
from .filters import CidadeFilter, PessoaFilter, CarroFilter, MoradorFilter, PorteiroFilter, VisitaFilter, ApartamentoFilter

from django.contrib.messages.views import SuccessMessageMixin



class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-cidade')
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    success_message = "Cidade %(nome)s adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidade'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar uma nova cidade.'
        context['botao'] = 'Cadastrar Cidade'
        return context

class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('list-pessoa')
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    success_message = "Pessoa %(nome_completo)s adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Pessoa'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar uma nova pessoa.'
        context['botao'] = 'Cadastrar Pessoa'
        return context

class CarroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Carro
    fields = ['placa', 'modelo', 'cor', 'apartamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-carro')
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    success_message = "Carro %(placa)s adicionado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Carro'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo carro.'
        context['botao'] = 'Cadastrar Carro'
        return context

class MoradorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Morador
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'apartamento', 'possui_animais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-morador')
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    success_message = "Morador %(nome_completo)s adicionado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Morador'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo morador.'
        context['botao'] = 'Cadastrar Morador'
        return context

class PorteiroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Porteiro
    fields = ['nome', 'turno']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-porteiro')
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    success_message = "Porteiro %(nome)s adicionado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Porteiro'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo porteiro.'
        context['botao'] = 'Cadastrar Porteiro'
        return context

class VisitaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Visita
    fields = ['pessoa_visita', 'pessoa_visitada', 'motivo', 'data_hora_entrada', 'data_hora_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-visita')
    login_url = reverse_lazy('login')
    group_required = "Administrador", "Usuarios"
    success_message = "Visita para %(pessoa_visitada)s adicionada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Visita'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar uma nova visita.'
        context['botao'] = 'Cadastrar Visita'
        return context

class ApartamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Apartamento
    fields = ['numero', 'bloco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-apartamento')
    login_url = reverse_lazy('login')
    group_required = "Administrador"
    success_message = "Apartamento %(numero)s adicionado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Apartamento'
        context['descricao'] = 'Preencha todos os campos obrigatórios para cadastrar um novo apartamento.'
        context['botao'] = 'Cadastrar Apartamento'
        return context

##########UPDATE##############

class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-cidade')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Cidade'
        context['descricao'] = 'Atualize os campos necessários para modificar a cidade existente.'
        context['botao'] = 'Atualizar Cidade'
        return context

class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('list-pessoa')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Pessoa'
        context['descricao'] = 'Atualize os campos necessários para modificar a pessoa existente.'
        context['botao'] = 'Atualizar Pessoa'
        return context

class CarroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Carro
    fields = ['placa', 'modelo', 'cor', 'apartamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-carro')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Carro'
        context['descricao'] = 'Atualize os campos necessários para modificar o carro existente.'
        context['botao'] = 'Atualizar Carro'
        return context

class MoradorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Morador
    fields = ['nome_completo', 'nascimento', 'cpf', 'email', 'cidade', 'apartamento', 'possui_animais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-morador')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Morador'
        context['descricao'] = 'Atualize os campos necessários para modificar o morador existente.'
        context['botao'] = 'Atualizar Morador'
        return context

class PorteiroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Porteiro
    fields = ['nome', 'turno']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-porteiro')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Porteiro'
        context['descricao'] = 'Atualize os campos necessários para modificar o porteiro existente.'
        context['botao'] = 'Atualizar Porteiro'
        return context

class VisitaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Visita
    fields = ['pessoa_visita', 'pessoa_visitada', 'motivo', 'data_hora_entrada', 'data_hora_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-visita')
    login_url = reverse_lazy('login')
    group_required = "Administrador", "Usuarios"

    def get_object(self, queryset=None):
        visita = self.object = Visita.objects.get(pk=self.kwargs['pk'])
        if not self.request.user.groups.filter(name='Administrador').exists():
            if self.object.user != self.request.user:
                raise AcessoNegado
        return visita

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Visita'
        context['descricao'] = 'Atualize os campos necessários para modificar a visita existente.'
        context['botao'] = 'Atualizar Visita'
        return context

class ApartamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Apartamento
    fields = ['numero', 'bloco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('list-apartamento')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Apartamento'
        context['descricao'] = 'Atualize os campos necessários para modificar o apartamento existente.'
        context['botao'] = 'Atualizar Apartamento'
        return context

#######DELETE#######

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-cidade')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-pessoa')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

class CarroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Carro
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-carro')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

class MoradorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Morador
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-morador')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

class PorteiroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Porteiro
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-porteiro')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

class VisitaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Visita
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-visita')
    login_url = reverse_lazy('login')
    group_required = "Administrador", "Usuarios"

    def get_object(self, queryset=None):
        visitaDelete = self.object = Visita.objects.get(pk=self.kwargs['pk'])
        if not self.request.user.groups.filter(name='Administrador').exists():
            if self.object.user != self.request.user:
                raise Acesso_Negado_voce_nao_tem_permissao_para_excluir_esta_visita
        return visitaDelete

class ApartamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Apartamento
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('list-apartamento')
    login_url = reverse_lazy('login')
    group_required = "Administrador"

#######LISTA#######

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Cidade
    filterset_class = CidadeFilter
    template_name = 'cadastros/listas/cidade.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

class PessoaList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Pessoa
    filterset_class = PessoaFilter
    template_name = 'cadastros/listas/pessoa.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

class CarroList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Carro
    filterset_class = CarroFilter
    template_name = 'cadastros/listas/carro.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

class MoradorList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Morador
    filterset_class = MoradorFilter
    template_name = 'cadastros/listas/morador.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

class PorteiroList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Porteiro
    filterset_class = PorteiroFilter
    template_name = 'cadastros/listas/porteiro.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

class VisitaList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Visita
    filterset_class = VisitaFilter
    template_name = 'cadastros/listas/visita.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

    #Lista apenas as visitas do usuario logado, exibe todas as visitas para o grupo Administrador
    def get_queryset(self):
        if self.request.user.groups.filter(name='Administrador').exists():
            return Visita.objects.all()
        return Visita.objects.filter(user=self.request.user)

class ApartamentoList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    model = Apartamento
    filterset_class = ApartamentoFilter
    template_name = 'cadastros/listas/apartamento.html'
    login_url = reverse_lazy('login')
    group_required = ("Administrador", "Usuarios")

