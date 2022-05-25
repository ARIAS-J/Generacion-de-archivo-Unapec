from django.urls import path
from . import views
urlpatterns = [
    path('home', views.generar_file, name="Generar_file" )
]