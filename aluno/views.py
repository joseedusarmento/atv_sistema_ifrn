from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# CRUD com CBV em Aluno

class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/alunos.html'
    context_object_name = 'alunos'

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'aluno/detalhe.html'
    context_object_name = 'aluno'
    
class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/form.html'
    success_url = reverse_lazy('alunos_list')

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/form.html'
    success_url = reverse_lazy('alunos_list')

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/confirm_delete.html'
    success_url = reverse_lazy('alunos_list')

def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    total_professores = Professor.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cidades' : total_cidades,
        'total_cursos' : total_curso,
        'total_professores' : total_professores
    }
    return render(request, "aluno/index.html",context)


def curso_listar(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, "curso/curso_listar.html", context)

def curso_criar(request):

    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CursoForm()
            return redirect("curso_listar")
    else:
        form = CursoForm()
    
    context= {
        'form': form
    }

    return render(request, "curso/form.html",context)

def curso_remover(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('curso_listar')

def curso_editar(request,id):
    curso = get_object_or_404(Curso,id=id)
   
    if request.method == 'POST':
        form = CursoForm(request.POST,request.FILES,instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_listar')
    else:
        form = CursoForm(instance=curso)

    return render(request,'curso/form.html',{'form':form})

def cidade_criar(request):

    if request.method == "POST":
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CidadeForm()
            return redirect("cidade_listar")
    else:
        form = CidadeForm()
    
    context= {
        'form': form
    }

    return render(request, "cidade/form.html",context)

def cidade_listar(request):
    cidades = Cidade.objects.all()
    context = {
        'cidades': cidades
    }
    return render(request, "cidade/cidade_listar.html", context)

def cidade_remover(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete()
    return redirect('cidade_listar')

def cidade_editar(request,id):
    cidade = get_object_or_404(Cidade,id=id)
   
    if request.method == 'POST':
        form = CidadeForm(request.POST,request.FILES,instance=cidade)
        if form.is_valid():
            form.save()
            return redirect('cidade_listar')
    else:
        form = CidadeForm(instance=cidade)

    return render(request,'cidade/form.html',{'form':form})

def professor_listar(request):
    professores = Professor.objects.all()
    context ={
        'professores': professores
    }
    return render(request, "professor/professor_listar.html",context)

def professor_criar(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("professor_listar")
    else:
        form = ProfessorForm()
        
    return render(request, "professor/form.html", {'form': form})

def professor_editar(request,id):
    professor = get_object_or_404(Professor,id=id)
   
    if request.method == 'POST':
        form = ProfessorForm(request.POST,instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_listar')
    else:
        form = ProfessorForm(instance=professor)

    return render(request,'professor/form.html',{'form':form})

def professor_remover(request, id):
    professor = get_object_or_404(Professor, id=id)
    professor.delete()
    return redirect('professor_listar')