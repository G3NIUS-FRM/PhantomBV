from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('crear_articulo', views.crear_articulo, name="crear_articulo"),
    path('eliminar_articulo', views.eliminar_articulo, name='eliminar_articulo')
]