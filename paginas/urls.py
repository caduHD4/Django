from django.urls import path
# Importar as views
from .views import IndexView, SobreView, LoginView, RegisterView

urlpatterns = [
    # Criar urls para as views
    path("", IndexView.as_view(), name ="index"),
    path("sobre/", SobreView.as_view(), name ="sobre"),
    path("login/", LoginView.as_view(), name ="login"),
    path("register/", RegisterView.as_view(), name ="register"),
]