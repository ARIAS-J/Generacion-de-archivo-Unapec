from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('document', views.generar_file, name="Generar_file" )
]