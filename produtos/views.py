from django.shortcuts import render

def listagem_produtos(request):
    context = {
        'produtos': [
            {'nome': 'Uva', 'preco': 1}, 
            {'nome': 'Melancia', 'preco': 10},
            {'nome': 'Banana', 'preco': 14}
        ]
    }
    return render(request, 'templates/listagem_produtos.html', context)
