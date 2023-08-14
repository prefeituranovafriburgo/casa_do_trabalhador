
from django.shortcuts import render, redirect
from .models import *
from autenticacao.models import Pessoa
from autenticacao.forms import Form_Pessoa
from .forms import EducacaoForm, ExperienciaProfissionalForm, PessoaCurriculoForm
from django.contrib import messages
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

def cadastrar_ou_aletarar_foto_e_objetivo(request):
    print(request.FILES)
    instance = Pessoa.objects.get(user=request.user)
    form_pessoa = Form_Pessoa(instance=instance)   
    form_objetivo= PessoaCurriculoForm( instance=instance)
    if request.method == 'POST':
        print(request.FILES)
        form_pessoa = Form_Pessoa(request.POST, instance=instance)
        form_objetivo= PessoaCurriculoForm(request.POST, request.FILES,instance=instance)
        if form_objetivo.is_valid():
            form_objetivo.save()
            messages.success(request, 'Dados do curriculo atualizados com sucesso!')
        if form_pessoa.is_valid():
            form_pessoa.save()
            messages.success(request, 'Dados pessoais atualizados com sucesso!')  
    print('foto:', instance.foto)
    context = {
        'form_objetivo': form_objetivo,
        'form_pessoa': form_pessoa,
        'foto': instance.foto,
    }
    return render(request, 'curriculo/cadastrar_ou_aletarar_foto_e_objetivo.html', context)