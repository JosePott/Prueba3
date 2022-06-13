from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')      
def nosotros(request):
    return render(request,'core/nosotros.html') 
def tienda(request):
    return render(request,'core/tienda.html') 
def donaciones(request):
    return render(request,'core/donaciones.html') 
def contacto(request):
    return render(request,'core/contacto.html') 
def Camas(request):
    return render(request,'core/camastienda.html') 
def Ropa(request):
    return render(request,'core/ropatienda.html') 
def Collares(request):
    return render(request,'core/collarestienda.html') 
