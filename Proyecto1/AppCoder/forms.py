from django import forms

class formSetEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class formSetCurso(forms.Form):
    nombre = forms.CharField(max_length=40)
    comision = forms.IntegerField()

class formSetProfesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email =  forms.EmailField()
    profesion = forms.CharField(max_length=30)

class formSetEntregable(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()            