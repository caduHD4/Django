from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import UsuarioCreate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='usuarios/login.html'
        ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
    template_name='usuarios/login.html',
    extra_context={'titulo': 'Alterar senha atual'},
    success_url=reverse_lazy('inicio')
), name="alterar-senha"),
    
        path('registrar/', UsuarioCreate.as_view(), name='registrar'),

]
