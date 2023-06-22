from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('curso/', curso, name="Curso"),
    path('profesor/', profesor, name="Profesores")
    path('estudiante/', estudiante, name="Estudiantes"),
    path('entregable/', entregable, name='Entregables'),    
    path('setEstudiante/',setEstudiantes, name="setEstudiante"),
]
