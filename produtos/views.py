from django.shortcuts import render

def listagem_produtos(request):
    produtos_dos_vendedores = [{
        'vendedor': {'nome': 'John Doe'},
        'produtos': [
            {'nome': 'Uva', 'preco': 1}, 
            {'nome': 'Melancia', 'preco': 10},
            {'nome': 'Banana', 'preco': 14}
        ]
    },
    {
        'vendedor': {'nome': 'Marta Doe'},
        'produtos': [
            {'nome': 'Maçã', 'preco': 5}, 
        ]
    }]
    context = {'produtos_dos_vendedores': produtos_dos_vendedores }
    return render(request, 'templates/listagem_produtos.html', context)
