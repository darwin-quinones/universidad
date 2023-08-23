from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

def home(request):
    cursos = Curso.objects.all()
    messages.success(request, '¡ Cursos Listados !')
    return render(request, 'gestionCursos.html', {'cursos': cursos})

def registrarCurso(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    creditos = request.POST['creditos']
    try :
        Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
        messages.success(request, 'Curso Registrado')
        return redirect('/')
    except:
        messages.error(request, '¡ El curso ya se encuentra registrado !')
        return redirect('/')
    

# aquí  se obtienen y se manda ala vista
def editarCurso(request, codigo):
    try :
        curso = Curso.objects.get(codigo=codigo)
        return render(request, 'editarCuso.html', {'curso': curso} )
    except:
        messages.error(request, 'El curso no existe !')
        return redirect('/')
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

