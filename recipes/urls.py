from django.urls import path

from recipes.views import cake, home, juice, pizza, temp

urlpatterns = [
    # Cliente solicitando uma request...
    path('', home),
    path('bolo/', cake),
    path('suco/', juice),
    path('pizza/', pizza),
    path('temp/', temp)
]
