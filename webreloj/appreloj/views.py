from django.shortcuts import render

# Create your views here.
def avance1 (request):
    return render(request, 'Avance1.html')

def Contacto (request):
    return render(request, 'Contacto.html')

def QuienesSomos (request):
    return render(request, 'QuienesSomos.html')

def Register (request):
    return render(request, 'Register.html')
