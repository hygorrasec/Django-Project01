from django.shortcuts import render  # Ler um arquivo e renderiza-lo


# Servidor respondendo a request solicitada pelo cliente...
def home(request):
    # Podemos alterar o diretório. Neste caso, está global no base_templates.
    return render(request, 'global/home.html', context={
        'name': 'Hygor Rasec'
    })


def temp(request):
    return render(request, 'pasta_provisoria/temp.html', context={
        'name': 'Hygor Rasec'
    })


def cake(request):
    return render(request, 'recipes/bolo.html', context={
        'name': 'Hygor Rasec'
    })


def pizza(request):
    return render(request, 'recipes/pizza.html', context={
        'name': 'Hygor Rasec'
    })


def juice(request):
    return render(request, 'recipes/suco.html', context={
        'name': 'Hygor Rasec'
    })
