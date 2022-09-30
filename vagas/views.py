# PARA AS VIEWS
from django.views.decorators.clickjacking import xframe_options_exempt
from multiprocessing import context
from django.shortcuts import render, redirect
# AUTH
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# MODELS E FORMS
from .forms import *
from django.contrib.auth.models import User
# OUTROS
from django.http import FileResponse, Http404
import requests
import pdfkit

# VIEWS
def home(request):    
    vagas_destaque=Vaga_Emprego.objects.filter(destaque=True)
    vagas=Vaga_Emprego.objects.filter(ativo=True)
    qnt_vagas=len(vagas)
    cont=0
    for i in vagas:
        cont+=i.quantidadeVagas
    context={
        'vagas': vagas_destaque,
        'qnt_cargos': qnt_vagas,
        'qnt_vagas': cont,
        'qnt_destaque': len(vagas_destaque)
    }
    return render(request, 'vagas/index.html', context)

@login_required
def cadastrar_empresa(request):
    if request.method=='POST':        
        form=Form_Empresa(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Empresa(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Empresa cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_empresa.html', context)  
    else:
        form=Form_Empresa(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_empresa.html', context)  

@login_required
def alterar_empresa(request, id):
    empresa=Empresa.objects.get(id=id)
    if request.method=='POST':        
        form=Form_Empresa(request.POST, instance=empresa)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Alterar',
                'form': Form_Empresa(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga alterada com sucesso!']
            }
            return redirect('vagas:empresas')
    else:
        
        form=Form_Empresa(instance=empresa)
    context={
        'form': form,
        'tipo_cadastro': 'Alterar',
    }
    return render(request, 'vagas/cadastrar_empresa.html', context)  

@login_required
def cadastrar_cargo(request):
    if request.method=='POST':        
        form=Form_Cargo(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Cargo(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_cargo.html', context)  
    else:
        form=Form_Cargo(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_cargo.html', context) 

@login_required
def alterar_cargo(request, id):
    cargo=Cargo.objects.get(id=id)
    if request.method=='POST':        
        form=Form_Cargo(request.POST, instance=cargo)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Alterar',
                'form': Form_Cargo(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga alterada com sucesso!']
            }
            return redirect('vagas:listar_cargos')
    else:
        
        form=Form_Cargo(instance=cargo)
    context={
        'form': form,
        'tipo_cadastro': 'Alterar',
    }
    return render(request, 'vagas/cadastrar_escolaridade.html', context)  

@login_required
def cadastrar_escolaridade(request):
    if request.method=='POST':        
        form=Form_Escolaridade(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Escolaridade(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_escolaridade.html', context)  
    else:
        form=Form_Escolaridade(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_escolaridade.html', context) 


@login_required
def alterar_escolaridade(request, id):
    escolaridade=Escolaridade.objects.get(id=id)
    if request.method=='POST':        
        form=Form_Escolaridade(request.POST, instance=escolaridade)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Alterar',
                'form': Form_Escolaridade(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga alterada com sucesso!']
            }
            return redirect('vagas:escolaridades')
    else:
        
        form=Form_Escolaridade(instance=escolaridade)
    context={
        'form': form,
        'tipo_cadastro': 'Alterar',
    }
    return render(request, 'vagas/cadastrar_escolaridade.html', context)  

@login_required
def cadastrar_vagaOfertada(request):
    if request.method=='POST':        
        gambiarra={}     
        for item in request.POST:
            if item=='cargo':
                try:
                    gambiarra[item]=Cargo.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            elif item=='empresa':
                try:
                    gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            else:
                gambiarra[item]=request.POST[item]
        form=CadastroVagasForm(gambiarra)             
        if form.is_valid():                  
            form.save()
            context={
                'tipo_cadastro': 'cadastrar',
                'form': CadastroVagasForm(initial={'ativo': True,'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_vagaOfertada.html', context)  
    else:
        form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
    context={
        'tipo_cadastro': 'cadastrar',
        'form': form,
        'hidden': ['user', 'ativo']
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

@login_required
def remover_vaga(request, id):
    if request.method=='POST':        
        try:
            vaga=Vaga_Emprego.objects.get(id=request.POST['remover'])
            vaga.ativo=False
            vaga.save()
            return redirect('vagas:vagas')
        except:
            pass
    context={
        'id': id,
        'vaga': Vaga_Emprego.objects.get(id=id)
    }
    return render(request, 'vagas/remover_vagaOfertada.html', context)

@login_required
def cadastrar_vaga_emLote(request):
    if request.method=='POST': 
        try:
            empresa=Empresa.objects.get(nome=request.POST['empresa'])
            success=True
        except:
            success=False
        if success:                        
            form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
            context={
                'empresa': request.POST['empresa'],
                'tipo_cadastro': 'cadastrar',
                'form': form,
                'hidden': ['user', 'ativo']
            }
            return render(request, 'vagas/cadastrar_vagas_emLote_2.html', context)
    form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
    context={
        'tipo_cadastro': 'cadastrar',
        'form': form,
        'hidden': ['user', 'ativo']
    }
    return render(request, 'vagas/cadastrar_vagas_emLote.html', context)

def cadastrar_candidato(request):
    if request.method=='POST': 
        pass

    form=Form_Candidato(request.POST)

    context={
        'tipo_cadastro': 'cadastrar',
        'form': form,
        'hidden': ['user', 'ativo']
    }

    return render(request, 'vagas/cadastrar_candidato.html', context)

def get_empresa(request):
    try:
        # empresas=Empresa.objects.filter(nome__startswith=request.GET.get('nome')).order_by('nome')
        empresas=Empresa.objects.filter(nome__icontains=request.GET.get('empresa')).order_by('nome')
    except Exception as E:
        print(E)
        empresas=None
    context={
        'results': empresas,
    }
    return render(request, 'vagas/resultEmpresaSearchs.html', context)


def get_cargo(request):
    try:
        # empresas=Empresa.objects.filter(nome__startswith=request.GET.get('nome')).order_by('nome')
        cargos=Cargo.objects.filter(nome__icontains=request.GET.get('vaga')).order_by('nome')
    except Exception as E:
        print(E)
        cargos=None
    context={
        'results': cargos,
    }
    return render(request, 'vagas/resultVagaSearchs.html', context)


def visualizar_vaga(request, id):
    if request.method=='POST':    
        gambiarra={}     
        for item in request.POST:
            if item=='vaga':
                gambiarra[item]=Cargo.objects.get(nome=request.POST[item]).id
            elif item=='empresa':
                gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
            else:
                gambiarra[item]=request.POST[item]
        form=CadastroVagasForm(gambiarra)    
        vaga=Vaga_Emprego.objects.get(id=id)         
        if form.is_valid():
                
            form=CadastroVagasForm(gambiarra, instance=vaga)  
            form.save()
            return redirect('vagas:vagas')
    else:        
        vaga=Vaga_Emprego.objects.get(id=id)
        form=CadastroVagasForm(instance=vaga)

    if request.user.is_authenticated:
        context={
            'id': id,
            'tipo_cadastro': '',
            'form': form,
            'hidden': ['user', 'ativo', 'destaque'],
            'cargo': vaga.cargo.nome,
            'empresa': vaga.empresa.nome
        }
    else:
        context={
                'id': id,
                'tipo_cadastro': '',
                'form': form,
                'hidden': ['user', 'ativo', 'destaque', 'empresa'],
                'cargo': vaga.cargo.nome,
                'empresa': vaga.empresa.nome
            }
    
    
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

@login_required
def alterar_vaga(request, id):
    if request.method=='POST':    
        gambiarra={}     
        for item in request.POST:
            if item=='cargo':
                try:
                    gambiarra[item]=Cargo.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            elif item=='empresa':
                try:
                    gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            else:
                gambiarra[item]=request.POST[item]
        form=CadastroVagasForm(gambiarra)    
        vaga=Vaga_Emprego.objects.get(id=id)         
        if form.is_valid():
                
            form=CadastroVagasForm(gambiarra, instance=vaga)  
            form.save()
            return redirect('vagas:vagas')
    else:        
        vaga=Vaga_Emprego.objects.get(id=id)
        form=CadastroVagasForm(instance=vaga)

    context={
        'id': id,
        'tipo_cadastro': 'Alterar',
        'form': form,
        'hidden': ['user', 'ativo'],
        'cargo': vaga.cargo.nome,
        'empresa': vaga.empresa.nome
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

def vagas(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True).order_by('cargo__nome'),
        'bairros': Empresa.objects.order_by('bairro').values_list('bairro').distinct(),
        'escolaridades': Escolaridade.objects.all().values()
    }
    return render(request, 'vagas/vagas_disponiveis.html', context)

def empresas(request):
    context={
        'empresas': Empresa.objects.all()
    }
    return render(request, 'vagas/listar_empresas.html', context)

def escolaridades(request):
    context={
        'escolaridades': Escolaridade.objects.all()
    }
    return render(request, 'vagas/listar_escolaridade.html', context)

def listar_cargos(request):
    context={
        'vagas': Cargo.objects.all()
    }
    return render(request, 'vagas/listar_cargos.html', context)

def imprimir_vagas(request):
    vagas=Vaga_Emprego.objects.filter(ativo=True).order_by('cargo__nome')    
    cont=0
    for i in vagas:
        cont+=i.quantidadeVagas


    context={
        'vagas': vagas,
        'total': cont
    }
    return render(request, 'vagas/imprimir_vagas.html', context)

@xframe_options_exempt
def vagas_table(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True)
    }
    return render(request, 'vagas/vagas.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        #Abaixo recebemos a validação da API do Google do reCAPTCHA
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LdiIsweAAAAADv7tYKHZ1fCP4pi6FwIZTw4X4Rl',
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        #Se o reCAPTCHA garantir que o usuário é um robô
        if result['success']:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    return redirect(request.GET['next'])    
                except:
                    return redirect('vagas:home')
            else:                
                context={
                    'error': True,
                }
                return render(request, 'registration/login.html', context)
        else:
            context={
                'error2': True,            
            }
            return render(request, 'registration/login.html', context)
    return render(request, 'registration/login.html')


def encaminhar(request, id):
    from datetime import date
    today = date.today()
    vaga=Vaga_Emprego.objects.get(id=id)
    if request.method=='POST':          
        context={
            'vaga': vaga,
            'date': today,
            'candidato': {'nome': request.POST['nome']}
        }        
        return render(request, 'vagas/encaminhar.html', context)
        
    return redirect('vagas:encaminhamento', id)


def encaminhamento(request, id, user_id=0): 
    candidato=Candidato.objects.get(id=id)
    if str(int(user_id))!=str(int(0)):
        user=User.objects.get(id=user_id)
    else:
        user=False

    from datetime import date
    today = date.today()    
    context={
                'vaga': candidato.vaga,
                'date': today,
                'candidato': candidato,
                'sistema': True,   
                'user': user             
            }
    return render(request, 'vagas/encaminhar.html', context)

def gera_encaminhamento_to_pdf(request, id, user_id=0):
    try:
        url_pdf='/home/casa_do_trabalhador/site/balcao_de_emprego/vagas/static/pdf/'+str(id)+'.pdf'    
        # url_pdf='/home/eduardo/projects/casadotrabalhador/vagas/static/pdf/'+id+'.pdf'    
        pdfkit.from_url('https://casadotrabalhador.pmnf.rj.gov.br/visualizar-vaga/alt0x'+str(id)+'0'+str(user_id)+'01/encaminhamento', url_pdf)        
        # pdfkit.from_url('http://localhost:8000/visualizar-vaga/alt0x'+str(id)+'0'+str(user_id)+'01/encaminhamento', url_pdf)        
        
        context={
            'pdf': url_pdf 
        }
        try:
            return FileResponse(open(url_pdf, 'rb'), content_type='application/pdf')
        except Exception as E:
            print(E)
            raise Http404()
    except Exception as E:
        print(E)
        return redirect('/')

def candidatarse(request, id):    
    if request.user.is_authenticated:

        form=Form_Candidato(initial={'vaga': id, 'candidato_online': False})
    else:
        form=Form_Candidato(initial={'vaga': id, 'candidato_online': True}) 

    if request.method=='POST':
        form=Form_Candidato(request.POST)
        if form.is_valid():
            candidato=form.save()                                   
            # return render(request, 'vagas/encaminhar.html', context)
            if request.user.is_authenticated:
                candidato.funcionario_encaminhamento=request.user
                candidato.save()
                return redirect('vagas:encaminhamento', id=candidato.id, user_id=request.user.id)
            return redirect('vagas:encaminhamento', id=candidato.id, user_id=0)

    context={
        'id': id,
        'form': form
    }
    return render(request, 'vagas/candidatarse.html', context)

@login_required
def candidatosporvaga(request, id):
    candidatos=Candidato.objects.filter(vaga=id).order_by('dt_inclusao')
    context={
        'candidatos': candidatos,
        'id': id
    }
    return render(request, 'vagas/listar_candidatos.html', context)

@login_required
def pesquisar_candidatos(request):
    context={}
    return render(request, 'vagas/pesquisar_candidatos.html', context) 

@login_required
def get_candidatos(request):
    try:
        # empresas=Empresa.objects.filter(nome__startswith=request.GET.get('nome')).order_by('nome')
        candidatos=Candidato.objects.filter(nome__icontains=request.GET.get('candidatos')).order_by('nome')
    except Exception as E:
        print(E)
        candidatos=None
    
    context={
        'candidatos': candidatos,
    }
    return render(request, 'vagas/pesquisar_candidatos_result.html', context)

@login_required
def visualizar_candidato(request, id):
    candidato=Candidato.objects.get(id=id)
    context={
        'candidato': candidato,
        'form': Form_Candidato(instance=candidato)
    }
    return render(request, 'vagas/pesquisar_candidatos_visualizar.html', context)

@login_required
def vagascomcandidatos(request):
    vagas=Vaga_Emprego.objects.filter(ativo=True)
    vagas_desativadas=Vaga_Emprego.objects.filter(ativo=False)
    balcao=0
    online=0
    balcao2=0
    online2=0
    vagas_com_candidatos=[]
    vagas_desativadas_com_candidatos=[]
    for vaga in vagas:
        candidatos=Candidato.objects.filter(vaga=vaga.id)                
        if len(candidatos)>0:
            vagas_com_candidatos.append(vaga)
            balcao_=Candidato.objects.filter(vaga=vaga.id, candidato_online=False)
            if len(balcao_)>0:
                balcao+=len(balcao_)
            online_=Candidato.objects.filter(vaga=vaga.id, candidato_online=True)
            if len(online_)>0:
                online+=len(online_)
            

    for vaga in vagas_desativadas:
        candidatos_desativados=Candidato.objects.filter(vaga=vaga.id)                
        if len(candidatos_desativados)>0:
            vagas_desativadas_com_candidatos.append(vaga)
            balcao_desativada=Candidato.objects.filter(vaga=vaga.id, candidato_online=False)
            if len(balcao_desativada)>0:
                balcao2+=len(balcao_desativada)
            online_desativada=Candidato.objects.filter(vaga=vaga.id, candidato_online=True)
            if len(online_desativada)>0:
                online2+=len(online_desativada)
    
    context={
        'vagas':vagas_com_candidatos,
        'balcao': balcao,
        'online': online,
        'balcao2': balcao2,
        'online2': online2
    }
    
    return render(request, 'vagas/vagas_com_candidatos.html', context)

@login_required
def candidatosporfuncionario(request):
    usuarios=User.objects.filter(groups__name='atendente')
    lista=[]
    for i in usuarios:
        lista.append([i.first_name, len(Candidato.objects.filter(funcionario_encaminhamento=i)), i.id])

    #deletar abaixo
    
    context={        
        'lista': lista
    }
    
    return render(request, 'vagas/candidatos_por_funcionarios.html', context)

@login_required
def funcionario_encaminhados(request, id):
    candidatos=Candidato.objects.filter(funcionario_encaminhamento=id)
    context={
        'candidatos': candidatos,
        'fulano': User.objects.get(id=id).first_name,
        'id': id
    }
    return render(request, 'vagas/candidatos_por_funcionarios_detalhe.html', context)


@login_required
def sair(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('vagas:home')
    else:
        return redirect('/accounts/login')