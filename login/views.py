from django.shortcuts import render, redirect
from .forms import Registro, Login
from django.contrib.auth import login
# Create your views here.
def registro_usuario(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # o a donde quieras
    else:
        form = Registro()
    return render(request,'registro.html',{"form":form})
def loggeate(request):
    if request.method == 'POST':
        form=Login(request.POST)
        print(form.errors)
        if form.is_valid():
            user=form.get_user()
            print(user)
            if user is not None:
                print("lo")
                login(request,user)
                return redirect("/")
            else:
                form.add_error(None, "Usuario o contrasena incorrecto")
    else:
        form=Login()
    return render(request, 'login.html', {"form":form})