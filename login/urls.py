from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registro_usuario, name="Registro"),
    path('', views.loggeate, name="login")
]