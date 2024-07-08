from django.contrib import admin
from .models import Cidade, Pessoa, Carro, Morador, Porteiro, Visita, Apartamento;

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Carro)
admin.site.register(Morador)
admin.site.register(Porteiro)
admin.site.register(Visita)
admin.site.register(Apartamento)