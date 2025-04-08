from django.shortcuts import render

from .models import CitaMedica

# Create your views here.

def citaMedicaIndex(request):
    citas = CitaMedica.objects.select_related('paciente', 'medico').all()
    return render(request, 'gestion_medica/CitaMedica.html', {'citas': citas})

