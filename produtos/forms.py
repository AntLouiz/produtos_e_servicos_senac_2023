from django.forms import ModelForm
from produtos.models import Produto

class ProdutoModelForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'anuciante', 'imagem']


class ServicoModelForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'anuciante', 'imagem']
