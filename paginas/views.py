from django.views.generic import TemplateView

#criar uma view para pagina inicial
# com herança para a classe TemplateView
# Create your views here.

class IndexView (TemplateView):
    template_name ="paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class LoginView(TemplateView):
    template_name = "paginas/login.html"

class RegisterView(TemplateView):
    template_name = "paginas/register.html"
