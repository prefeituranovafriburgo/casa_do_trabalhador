
from django.shortcuts import render, redirect
from .models import *
from autenticacao.models import Pessoa
from .forms import EducacaoForm, ExperienciaProfissionalForm


# Create your views here.
def index(request):
    return render(request, 'curriculo/index.html')

def curriculo(request):
    pessoa = Pessoa.objects.get(user=request.user)
    educacoes = Educacao.objects.filter(pessoa=pessoa)
    experiencias = ExperienciaProfissional.objects.filter(pessoa=pessoa)

    context = {
        'nome': pessoa.nome,
        'email': pessoa.email,
        'telefone': pessoa.telefone,
        'objetivo': pessoa.objetivo,
        'educacoes': educacoes,
        'experiencias': experiencias,
    }
    return render(request, 'curriculo/curriculo.html', context)

def cadastrar_educacao(request):
    if request.method == 'POST':
        form = EducacaoForm(request.POST)
        if form.is_valid():
            educacao = form.save()
            educacao.pessoa=Pessoa.objects.get(user=request.user)
            educacao.save()
            form = EducacaoForm()
    else:
        form = EducacaoForm()
    pessoa=Pessoa.objects.get(user=request.user)
    context = {
        'form': form,
        'educacoes': Educacao.objects.filter(pessoa=pessoa)
    }
    return render(request, 'curriculo/cadastrar_educacao.html', context)

def excluir_educacao(request, id):
    if request.user.is_authenticated:
        educacao=Educacao.objects.get(id=id)
        pessoa=Pessoa.objects.get(user=request.user)
        if educacao.pessoa==pessoa:
            educacao.delete()
    return redirect('cv:educacao')

def excluir_experiencia(request, id):
    if request.user.is_authenticated:
        exp=ExperienciaProfissional.objects.get(id=id)
        pessoa=Pessoa.objects.get(user=request.user)
        if exp.pessoa==pessoa:
            exp.delete()
    return redirect('cv:educacao')
   
def cadastrar_experiencia(request):
    pessoa=Pessoa.objects.get(user=request.user)
    if request.method == 'POST':
        form = ExperienciaProfissionalForm(request.POST)
        if form.is_valid():
            exp=form.save()
            exp.pessoa=pessoa
            exp.save()
             # Redireciona para a página principal após o cadastro
    else:
        form = ExperienciaProfissionalForm()
    
    context = {
        'form': form,
        'experiencias': ExperienciaProfissional.objects.filter(pessoa=pessoa)
    }
    return render(request, 'curriculo/cadastrar_experiencia.html', context)