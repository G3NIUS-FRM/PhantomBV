from django.shortcuts import render, redirect, get_object_or_404
from articles.models import Articles
from users.models import CustomUser
from .forms import CrearArticulo
# Create your views here.
def home(request):

    articulos=Articles.objects.all().order_by('-creation_date')[:10]
    
    
    return render(request, "home.html", {"user":request.user , "articulos":articulos})
def crear_articulo(request):
    if request.method == "POST":
        form=CrearArticulo(request.POST)
        if form.is_valid():
            articulo=form.save(commit=False)
            articulo.autor=request.user
            articulo.save()
            return redirect('/')
    else:
        form=CrearArticulo()
    return render(request, "crear_articulo.html", {"form":form})
def eliminar_articulo(request):
    
    dato= request.POST.get('elim')

    elim=get_object_or_404(Articles, id=dato)
    elim.delete()
    print('Borrado con exito')
    return redirect('/')