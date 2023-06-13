from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('curso/', curso),
    path('profesor/', profesor),
    path('estudiante/', estudiante),
    path('entregable/', entregable),    
]
