from django.shortcuts import render

def usuarioIndex(request):
    return render(request, 'usuarios/Usuario.html')  # Asegúrate de tener esta plantilla
