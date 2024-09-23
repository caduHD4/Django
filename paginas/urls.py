from django.urls import path
# Importar as views
from .views import IndexView, SobreView

urlpatterns = [
    # Criar urls para as views
    path("", IndexView.as_view(), name ="inicio"),
    path("sobre/", SobreView.as_view(), name ="sobre"),
]