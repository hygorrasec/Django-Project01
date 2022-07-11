from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Cliente solicitando uma request...
    path('admin/', admin.site.urls, name='admin'),
    path('', include('recipes.urls'))
]
