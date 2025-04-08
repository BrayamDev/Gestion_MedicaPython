from django.db import models

from usuarios.models import Medico, Paciente


class EstadoCita(models.TextChoices):
    PROGRAMADA = 'Programada'
    CANCELADA = 'Cancelada'
    FINALIZADA = 'Finalizada'

class CitaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo_consulta = models.TextField()
    estado = models.CharField(max_length=20, choices=EstadoCita.choices, default=EstadoCita.PROGRAMADA)

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    diagnostico = models.TextField()
    tratamiento = models.TextField()

class ExamenMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_examen = models.CharField(max_length=100)
    resultados = models.TextField()

class VisitaSucesiva(models.Model):
    historial_clinico = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    fecha_visita = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField()

class ExamenFisico(models.Model):
    historial_clinico = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    tension_arterial = models.CharField(max_length=20)
    frecuencia_cardiaca = models.IntegerField()
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    talla = models.DecimalField(max_digits=4, decimal_places=2)

class EnfermedadBase(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_diagnostico = models.DateField()
    controlada = models.BooleanField(default=False)
