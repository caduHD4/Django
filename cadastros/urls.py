from django.urls import path
from .views import (
    CidadeCreate, PessoaCreate, CarroCreate, MoradorCreate, PorteiroCreate, VisitaCreate, ApartamentoCreate,
    CidadeUpdate, PessoaUpdate, CarroUpdate, MoradorUpdate, PorteiroUpdate, VisitaUpdate, ApartamentoUpdate,
    CidadeDelete, PessoaDelete, CarroDelete, MoradorDelete, PorteiroDelete, VisitaDelete, ApartamentoDelete,
    CidadeList, PessoaList, CarroList, MoradorList, PorteiroList, VisitaList, ApartamentoList
)

urlpatterns = [
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='add-cidade'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='add-pessoa'),
    path('cadastrar/carro/', CarroCreate.as_view(), name='add-carro'),
    path('cadastrar/moradore/', MoradorCreate.as_view(), name='add-morador'),
    path('cadastrar/porteiro/', PorteiroCreate.as_view(), name='add-porteiro'),
    path('cadastrar/visita/', VisitaCreate.as_view(), name='add-visita'),
    path('cadastrar/apartamento/', ApartamentoCreate.as_view(), name='add-apartamento'),

    ######UPDATE#######

    path('atualizar/cidades/<int:pk>/', CidadeUpdate.as_view(), name='update-cidade'),
    path('atualizar/pessoas/<int:pk>/', PessoaUpdate.as_view(), name='update-pessoa'),
    path('atualizar/carros/<int:pk>/', CarroUpdate.as_view(), name='update-carro'),
    path('atualizar/moradores/<int:pk>/', MoradorUpdate.as_view(), name='update-morador'),
    path('atualizar/porteiros/<int:pk>/', PorteiroUpdate.as_view(), name='update-porteiro'),
    path('atualizar/visitas/<int:pk>/', VisitaUpdate.as_view(), name='update-visita'),
    path('atualizar/apartamentos/<int:pk>/', ApartamentoUpdate.as_view(), name='update-apartamento'),
    
    ######DELETE######

    path('excluir/cidades/<int:pk>/', CidadeDelete.as_view(), name='delete-cidade'),
    path('excluir/pessoas/<int:pk>/', PessoaDelete.as_view(), name='delete-pessoa'),
    path('excluir/carros/<int:pk>/', CarroDelete.as_view(), name='delete-carro'),
    path('excluir/moradores/<int:pk>/', MoradorDelete.as_view(), name='delete-morador'),
    path('excluir/porteiros/<int:pk>/', PorteiroDelete.as_view(), name='delete-porteiro'),
    path('excluir/visitas/<int:pk>/', VisitaDelete.as_view(), name='delete-visita'),
    path('excluir/apartamentos/<int:pk>/', ApartamentoDelete.as_view(), name='delete-apartamento'),

    #######LISTA#######

    path('listar/cidades/', CidadeList.as_view(), name='list-cidade'),
    path('listar/pessoas/', PessoaList.as_view(), name='list-pessoa'),
    path('listar/carros/', CarroList.as_view(), name='list-carro'),
    path('listar/moradores/', MoradorList.as_view(), name='list-morador'),
    path('listar/porteiros/', PorteiroList.as_view(), name='list-porteiro'),
    path('listar/visitas/', VisitaList.as_view(), name='list-visita'),
    path('listar/apartamentos/', ApartamentoList.as_view(), name='list-apartamento'),


]
