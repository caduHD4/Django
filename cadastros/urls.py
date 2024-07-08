from django.urls import path
from .views import CidadeCreate, PessoaCreate, CarroCreate, MoradorCreate, PorteiroCreate, VisitaCreate, ApartamentoCreate

urlpatterns = [
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='add-cidade'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='add-pessoa'),
    path('cadastrar/carro/', CarroCreate.as_view(), name='add-carro'),
    path('cadastrar/moradore/', MoradorCreate.as_view(), name='add-morador'),
    path('cadastrar/porteiro/', PorteiroCreate.as_view(), name='add-porteiro'),
    path('cadastrar/visita/', VisitaCreate.as_view(), name='add-visita'),
    path('cadastrar/apartamento/', ApartamentoCreate.as_view(), name='add-apartamento'),

]
