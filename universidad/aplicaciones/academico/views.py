from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    messages.success(request, '¡ Cursos Listados !')
    return render(request, 'gestionCursos.html', {'cursos': cursos})

def registrarCurso(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    creditos = request.POST['creditos']
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, 'Curso Registrado')
    return redirect('/')

# aquí  se obtienen y se manda ala vista
def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'editarCuso.html', {'curso': curso} )

# aquí se editar el curso

def editCurso(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    creditos = request.POST['creditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request, 'Curso editado')
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, 'Curso Eliminado')
    return redirect('/')

