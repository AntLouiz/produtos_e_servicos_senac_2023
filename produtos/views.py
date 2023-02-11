from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from produtos.forms import ProdutoModelForm

def listagem_produtos(request):
    produtos = Produto.objects.filter(excluido=False)
    produtos_dos_vendedores = [{
        'vendedor': {'nome': 'John Doe'},
        'produtos': produtos
    }]
    context = {'produtos_dos_vendedores': produtos_dos_vendedores }
    return render(request, 'templates/listagem_produtos.html', context)

def detalhamento_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    context = {
        'produto': produto
    }
    return render(request, 'templates/detalhamento_produto.html', context)


def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/produtos/')

    form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'templates/cadastrar_produto.html', context)


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        produto.excluido = True
        produto.save()
        return HttpResponseRedirect('/produtos/')

    context = {
        'produto': produto
    }
    return render(request, 'templates/excluir_produto.html', context)
