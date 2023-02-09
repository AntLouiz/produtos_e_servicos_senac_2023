from django.urls import path
from .views import listagem_produtos, detalhamento_produto, cadastro_produto

urlpatterns = [
    path('', listagem_produtos),
    path('<int:id>', detalhamento_produto),
    path('cadastrar', cadastro_produto)
]
