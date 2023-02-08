from django.urls import path
from .views import listagem_produtos

urlpatterns = [
    path('', listagem_produtos)
]
