# PARA AS VIEWS
from django.views.decorators.clickjacking import xframe_options_exempt
from multiprocessing import context
from django.shortcuts import render, redirect
# AUTH
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# MODELS E FORMS
from .forms import *
# OUTROS
import requests

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
        'vagas': Vaga_Emprego.objects.filter(ativo=True).order_by('cargo__nome')
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
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True).order_by('cargo__nome')
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

@login_required
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


@login_required
def encaminhamento(request, id):    
    context={
        'id': id
    }
    return render(request, 'vagas/encaminhamento.html', context)

def candidatarse(request, id):    
    if request.user.is_authenticated:
        form=Form_Candidato(initial={'vaga': id})
    else:
        form=Form_Candidato(initial={'vaga': id, 'candidato_online': True}) 

    if request.method=='POST':
        form=Form_Candidato(request.POST)
        if form.is_valid():
            form.save()
            from datetime import date
            today = date.today()
            vaga=Vaga_Emprego.objects.get(id=id)
            context={
                'vaga': vaga,
                'date': today,
                'candidato': {'nome': request.POST['nome']},
                'sistema': True

            }        
            return render(request, 'vagas/encaminhar.html', context)

    context={
        'id': id,
        'form': form
    }
    return render(request, 'vagas/candidatarse.html', context)

@login_required
def candidatosporvaga(request, id):
    candidatos=Candidato.objects.filter(vaga=id)
    context={
        'candidatos': candidatos,
        'id': id
    }
    return render(request, 'vagas/listar_candidatos.html', context)

@login_required
def vagascomcandidatos(request):
    vagas=Vaga_Emprego.objects.filter(ativo=True)
    vagas_com_candidatos=[]
    for vaga in vagas:
        candidatos=Candidato.objects.filter(vaga=vaga.id)
        balcao=Candidato.objects.filter(vaga=vaga.id, candidato_online=False)
        online=Candidato.objects.filter(vaga=vaga.id, candidato_online=True)
        if len(candidatos)>0:
            vagas_com_candidatos.append(vaga)

    context={
        'vagas':vagas_com_candidatos,
        'balcao': len(balcao),
        'online': len(online)
    }
    
    return render(request, 'vagas/vagas_com_candidatos.html', context)


def gambiarra(request):
    empresas=[
        (2,'Mercado Arthur Ribeiro','10387548000190','Rua Téofilo Marra, 05 Cordoeira','2225238174','mercadoirmaosribeiro@hotmail.com','2022-05-11 14:30:57.178942',5,0,1,0,0,'','',0),
        (3,'Borrachão','08773664000103','Av. Gov. Roberto Silveira, 2040 Prado','2225271912','borrachao.fiscal@hotmail.com','2022-05-11 14:33:19.237961',5,0,1,1,1,'','',0),
        (4,'Rosenge Construções e Serviços Ltda','03109322000161','Rua da Conceição, 105 – Sala 1807 – Centro','2125240243','priscilapereira@rosenge.com.br','2022-05-11 14:38:19.915330',5,0,1,0,0,'','',0),
        (5,'Tetra Lingerie','12421275000188','Alameda Salomão Salles, 115 Jardim Ouro Preto','2225230878','rh.tetralingerie@hotmail.com','2022-05-11 14:44:53.187107',5,1,1,0,0,'','',0),
        (6,'Renner','92754738043481','Rua Moises Amelio, 17 loja 117- Cadima Shopping – Centro','27999006697','atendimento@lojasrenner.com.br','2022-05-11 14:49:44.162864',5,0,0,0,1,'','',0),(7,'Drogaria H7','01404097000160','Av. Alberto Braune, 276 loja 274','2225232412','erthalcoutoltda@hotmail.com','2022-05-11 14:52:31.924993',5,0,0,1,0,'','',0),(8,'Solução Service','12900021000142','Av. Euterpe Friburguense, 118','2225211303','livia@solucaomulti.com.br','2022-05-11 14:54:02.850620',5,0,1,0,0,'','',0),(9,'Neycar Auto Socorro','07313713000154','Rua Clarindo da Rosa Teixeira – 02 fundos – Prado','2225270107','curriculoneycar@bol.com.br','2022-05-11 14:57:42.693441',5,0,1,0,0,'','',0),(10,'Quarup Combustíveis','27650357000171','Rodovia RJ 116, km 73 Mury','2225421545','quarup@quarup.com','2022-05-11 15:00:51.791335',5,0,0,1,0,'','',0),(11,'Mamissushi Yakisoba','33913597000114','Av. Euterpe Friburguense - Centro','22997817809','yakisoba@yakisoba.com','2022-05-11 15:09:51.743437',5,0,0,0,1,'','',0),(12,'Subway Odf Cadima','24443321000129','Rua Moisés Amélio, 17 loja 241 Centro','2225239589','subwaycadimanf@hotmail.com','2022-05-11 15:21:54.564222',5,0,1,1,0,'','',0),(13,'Sabor D’Casa Bistrô','40416057000190','Praça Pres. Getúlio Vargas, 139 , Friburgo Shopping,2 °piso','22992367325','sabordcasanf@gmail.com','2022-05-11 15:25:44.950158',5,0,1,0,1,'','',0),(14,'Coca Cola Andina','00074569000100','Av. Antonio Mário de Azevedo 3333 – Corrego D’antas','21999310980','recrutamentorj@koandina.com','2022-05-11 17:03:35.848855',5,0,1,0,0,'','',0),(15,'DUDA Construção Civil','07049980000166','Av. Antonio Mário de Azevedo 6103 – Corrego D’antas','22992178304','dp@damewer.com.br','2022-05-11 17:05:33.750250',5,0,1,0,1,'','',0),(16,'Itaipava Tintas','36536936000693','Av. Euterpe Friburguense 150, Centro','24988399965','recrutamento@itaipavatintas.com.br','2022-05-11 17:07:24.542274',5,0,1,0,0,'','',0),(17,'Donaldo Transportes','29918268000199','Av. Antonio Mário de Azevedo. 5657 – Galpão 1 – C. Dantas','22988329610','matheus.donaldo@gmail.com','2022-05-11 17:10:31.386248',5,0,1,0,1,'','',0),(18,'Hotel Fazenda Caledônia Inn','08599055000171','Estrada Ayrton Senna da Silva Cascatinha','2225223313','rh@hotelcaledoniainn.com.br','2022-05-11 17:13:14.839365',5,0,1,0,1,'','',0),(19,'PBS Brasil','08051446000157','Rua Nicolau Gachet – 75 b Bairro Suiço','2241050029','mabellerosa@pbsbrasil.com.br','2022-05-11 17:15:26.765861',5,0,1,0,1,'','',0),(20,'Service Car Auto Mecânica','08057496000141','Rua Ortigão 8 – Centro','2225289504','src@src.com','2022-05-11 17:17:07.318227',5,0,0,1,1,'','',0),(21,'Andina','00000000000000','Rua Cardinot, 99 - Conselheiro','2226215314','recrutamentorj@koandina.com','2022-05-11 17:20:21.374000',5,0,1,0,0,'','',0),(22,'Ferreiro da Serra','15833314000142','Av. Walter Machado Tedim 5042 Mury','22999148528','contato@ferreirodaserra.com','2022-05-11 17:21:50.673444',5,0,1,1,1,'','',0),(23,'Express Informática','09169643000138','Rua Monsenhor José Antonio Teixeira 24 Centro','2225210323','expressnf@hotmail.com','2022-05-11 17:23:24.139029',5,0,1,0,1,'','',0),(24,'MPE Engenharia e Serviços','04743858000105','Rua São Francisco Xavier, Maracanã 603','22999220703','aline.pinto@mpeengenharia.com.br','2022-05-11 17:25:12.338142',5,0,1,0,1,'','',0),(25,'Motel Night and Day','28606242000142','Av. Antonio Mario de Azevedo, 1598 – Duas Pedras','22992267507','mot@mot.com','2022-05-11 17:31:55.210280',5,0,0,0,1,'','',0),(26,'SWIFT - Mercado de Carnes','02914460019331','Av. Walter Machado Thedim, 400 Mury','1131444000','polyana.freitas@swift.com.br','2022-05-11 18:19:32.269703',5,0,1,0,0,'','',0),(27,'Mar e Sam','02437258000185','Rua Marechal Floriano Peixoto 228 – Perissê','2225261361','maresamlingerie@hotmail.com','2022-05-11 18:24:27.761644',5,0,1,0,1,'','22998280125',0),(28,'Filó S/A','30535975000185','Rua Bonfim, 25 Vila Amélia','22997713423','','2022-05-11 18:26:17.168530',5,0,0,1,0,'','',0),(29,'Mística Moda e Lingerie','11403887000185','Rua Genecília Borges, Vargem Grande - Cônego','22998357999','','2022-05-11 18:28:13.567891',5,0,0,0,1,'','',0),(30,'Pureza Íntima Confecções','08922035000190','Av. Coronel Laudemiro das Mercês – 211 lote 30 Duas Pedras','2230160717','rh@purezaintima.com.br','2022-05-11 18:31:07.807777',5,0,1,0,1,'','',0),(31,'Choperia Monte Líbano','27234597000195','Rua Monte Líbano, 34 Centro','22998399498','marlon_ecard@yahoo.com','2022-05-11 18:34:13.107705',5,0,1,0,0,'','22998399498',1),(32,'Ouverney Gastronomia','01579437000194','Av. Walter Machado Thedim, 8600 RJ 116 – Km 78 - Debossan','22974023742','','2022-05-11 18:36:26.674379',5,0,0,0,0,'','22974023742',1),(33,'VLB Hotelaria Ltda','38300280000126','Av. Antonio Mário de Azevedo, 2775 Corrego D’antas','2225293451','diretoria@vilaverdehotel.com.br','2022-05-11 18:39:34.088419',5,0,1,1,0,'','',0),(34,'LBV','33915604011828','Av. Júlio Antônio Thurler Olaria','2225225078','leonelf@lbv.org.br','2022-05-11 18:41:42.943581',5,0,1,1,0,'','',0),(35,'SOS Elétrica','27086770000155','Rua Eugenia Schottz, 11 Corrego D’antas','22999683012','robsonfariar@yahoo.com.br','2022-05-11 18:45:53.765912',5,0,1,0,0,'','22999683012',1),(36,'Define - Plataforma de Ensino','22653914000275','Rua Nelson Kemp, 55 - Braunes','22981600182','atendimento@resolveeducacao.com.br','2022-05-11 18:48:14.143874',5,0,1,0,1,'','',0),(37,'Centro de Nefrologia de NF','02152491000111','Rua General Osório, 324 Centro','2225330228','cmnf.nefroterapia@gmail.com','2022-05-11 18:49:17.379541',5,0,1,1,0,'','',0),(38,'Tração Mania Peças e Acessórios','00131734000100','Av. Roberto Silveira, 1070 – Jd Ouro Preto','2225221214','lourdes@tracaomania.com.br','2022-05-11 18:50:38.741013',5,0,1,0,0,'','',0),(39,'Destemida Pizzaria','27282732000178','Av. Conselheiro Julius Arp 80 – bloco 10 - ARP','22981212627','contato.agmpizzaria@gmail.com','2022-05-11 18:52:51.635419',5,1,1,0,1,'','',0),(40,'Condomínio Parque das Magnólias','27765114000189','Rua Maria D’angelo Magliano, 159 – Olaria','2225215663','valadaoeviana@hotmail.com','2022-05-11 18:54:47.305048',5,1,1,0,0,'','22988439102',1),(41,'Brastoni Industrias','05416927000120','Rua Berlin 71 – Rio Grandina','2225401583','lucianabrastoni@hotmail.com','2022-05-11 18:56:34.065091',5,0,1,0,0,'','',0),(42,'RE Herdy Móveis Planejado','33663687000102','Casa do Trabalhador','22988310639','','2022-05-11 18:59:23.643891',5,0,0,1,0,'','',0),(43,'Hoteleira','30096051000120','Cantagalo','22981489122','recrutamento30122020@gmail.com','2022-05-11 19:02:05.872321',5,1,1,0,1,'','',0),(44,'Longo Auto Center','07795971000114','Rua Coronel João Teixeira 120 –Conselheiro - Fundos','2225271747','longoautocenter@hotmail.com','2022-05-11 19:03:14.200685',5,0,1,1,1,'','',0),(45,'Transrio Caminhões','11726521000490','Av. Engenheiro Hans Gaiser 650','2225231155','lilia.sanches@transrio.com.br','2022-05-11 19:04:36.506546',5,0,1,1,0,'','',0),(46,'TF Pneus','30001563000165','Avenida Antonio Mário de Azevedo - Km 19 - Conquista','2225434012','tfpneus.friburgo@hotmail.com','2022-05-11 19:10:43.198289',5,1,1,1,0,'','22981235602',1),(47,'Nova Boys','17697852000182','Avenida Conselheiro Julius Arp, 406 – Olaria','2225234141','','2022-05-11 19:12:59.213643',5,1,0,1,1,'','',0),(48,'Flash Boys','33432547000115','Rua Manoel Floriano Peixoto, 117 - Perissê','2225332224','','2022-05-11 19:14:20.677698',5,1,0,0,1,'','',0),(49,'CETEST Rio','39128525000142','Av. Passos, 120 – 17° andar Centro','2131847600','recrutad2022@yahoo.com','2022-05-11 19:16:43.396492',5,0,1,0,1,'','',0),(50,'Via Varejo Casas Bahia','33041260119641','Rua João Pessoa, 93 – São Caetano do Sul – SP','11992786355','sabrina.teixeira-ext@via.com.br','2022-05-11 19:19:40.500386',5,0,1,0,0,'','',0),(51,'Casa E Vídeo','11114284001801','Rua Moisés Amélio, 17 loja 210 Centro','22992319035','francisco.ferreira@casaevideo.com','2022-05-11 19:21:09.370883',5,0,1,0,0,'','22992319035',1),(52,'ENGEPRAT  Engenharia Ltda','03314057000153','Rua Anchieta, 364 - Atrás da HAGA','22999781693','','2022-05-11 19:22:26.414200',5,0,0,0,1,'','',0),(53,'Mister Submarine/Senhor Pizza','33946239000108','Rua Moisés Amélio, 17 loja 237 e 239 – Centro','','','2022-05-11 19:23:58.854820',5,0,0,1,0,'','',0),(54,'Index Centro de Ensino','08741691000196','Rua Moisés Amélio, 23 Centro','2225238777','indexnovafriburgo.comercial@cursoindex.com.br','2022-05-11 19:25:20.557587',5,0,1,1,0,'','',0),(55,'Sorria Rio','40594367000103','Rua Modesto de Mello, 11 – Centro','2232612683','','2022-05-11 19:26:24.292703',5,0,0,1,0,'','',0),(56,'Luandre Consultoria','04144144000687','Rua Evaristo da Veiga, 55 - 2° andar','2122202428','luanda.santos@luandre.com.br','2022-05-11 19:27:49.142894',5,0,1,0,1,'','',0),(57,'Motel Magnos','29283918000177','Rua Otilia Pereira Schuabb – Ponte da Saudade','2225225061','magnosmotel@gmail.com','2022-05-11 19:29:59.891533',5,0,1,1,1,'','',0),(58,'Supermercado Serra Azul','11820069000269','Estrada Antonio Acácio Cardinot – Parque Maria Tereza','22992915175','','2022-05-12 12:40:27.025286',5,1,0,1,0,'','22992915175',1),(59,'Agropatas Comércio de Menezes','11086462000190','Av. Manoel Carneiro de Menezes - Mury','2225422256','agropatas.racao@gmail.com','2022-05-12 12:43:31.781063',5,0,1,1,0,'','',0),(60,'Alpiserra','32772762000100','Rua Gonçalves Dias- Valparaiso','2422350050','curriculo@alpiserra.com.br','2022-05-12 12:44:37.212500',5,0,1,0,0,'','24988578939',1),(61,'Sodexo do Brasil','49930514333371','Sebastião Martins, 871 – Conselheiro Paulino','22997375437','marcelle.ferraz@sodexo.com','2022-05-12 12:46:54.092487',5,0,1,1,0,'','',0),(62,'INFO instalações em Fibra Óptica','24450752000112','Av. Tancredo Neves, 390','21982099980','raphael.baia@infoinstalacoes.com.br','2022-05-12 12:50:20.675282',5,0,1,0,0,'','21982099980',1),(63,'LINKO Group','34061730000114','Av. Jane Maria Marins Figueira – Jardim Mariléa','22999741489','curriculos@linkogroup.com','2022-05-12 12:51:37.598335',5,0,1,0,0,'','',0),
        (64,'Claro','02917443000177','Rua Camerino, 90 – Centro','21992052064','karina.fonseca@brasilcenter.com.br','2022-05-12 12:53:25.268013',5,0,1,0,0,'','21992052064',1),(65,'Jornal Casa Tudo','37689371000132','Rua Dr, Ernesto Brasílio, 14 Centro','22992631538','jornalcasatudo@gmail.com','2022-05-12 12:54:24.991298',5,0,1,0,0,'','',0),(66,'WK Promoção GS Saúde','36474831000142','Rua Nossa Senhora de Fátima, 12 – Centro','22997587596','','2022-05-12 12:55:45.675961',5,1,0,0,1,'','2225226080',0),(67,'Araújo Cell','41201338000199','Av. Alberto Braune, 29 – Centro','22999655951','araujocell709@gmail.com','2022-05-12 12:57:38.707084',5,0,1,0,0,'','22999285875',1),(68,'Sonho dos Pés','24811559000160','Av. Alberto Braune, 27 – Centro','22988176472','ingrid.roeber12@gmail.com','2022-05-12 12:59:17.970592',5,0,1,1,0,'','',0),(69,'Vivo Cadima Shopping','03685001001420','Rua Moisés Amélio, 17','2225237957','cronocadima@gmail.com','2022-05-12 13:01:47.635531',5,0,1,1,0,'','',0),(70,'Tapa Fácil Telhas/Madeiras','43904298000177','Av. Antonio Mario de Azevedo, 3308 – Corrego D’antas','2220102220','','2022-05-12 13:02:52.853459',5,0,0,1,0,'','22992260212',1),(71,'Labelly Lingerie','09429151000134','Av. Walter Machado Thedim, 949 – Mury','22999862996','labellylingerie2018@gmail.com','2022-05-12 13:06:38.038106',5,0,1,0,1,'','',0),(72,'Rospauth','10942185001006','Praça Presidente Getúlio Vargas, 202 - Centro','22999175501','rjdasilva2018@hotmail.com','2022-05-12 13:10:30.456307',5,0,1,1,1,'','',0),(73,'Master Friburgo Comercial','00095939000187','Av. Antônio Mário de Azevedo 2068 - Corrego D’antas','2225234979','mastergas@gigalink.com.br','2022-05-17 14:40:13.807530',5,0,1,0,0,'','22999619023',1),(74,'Big Blue','10482618000199','','','supermercadobigbluerh@gmail.com','2022-08-19 14:27:14.022080',5,1,1,0,0,'','',0),(75,'GA Decorações','03421986000161','Rua Oliveira Botelho - 32 Centro','2225226100','','2022-08-19 15:11:07.132789',5,1,0,1,0,'','',0),(76,'MA Pinheiro da Silva Contabilidade','13924933000117','Av. Conselheiro Julius Arp, 80 - Bloco 9/Sala 11 - Centro','2225236031','cristianodias@rcconsultoria.net','2022-08-19 18:00:40.394015',5,1,1,0,0,'','',0),(77,'Valcar Diesel','73880429000194','Rua Concórdia, Prado','2225272438','valcardiesel@gmail.com','2022-08-19 18:01:45.489186',5,1,1,0,0,'','22997606044',1),(78,'Chimarron','05027798000189','Rua Duque de Caxias – Nº 01 – Cobertura Centro','2225229090','lalegrealta@gmail.com','2022-08-19 18:04:29.760296',5,1,1,0,0,'','',0),(79,'DS Car','14116072000103','Cardinot, Av. Floresta 58b','2220100120','dpessoal@dscar.ind.br','2022-08-19 18:05:20.998014',5,1,1,0,0,'','',0),(80,'Hardyn','29278784000104','Rua Urbano Bachini, 32 Córrego D’antas','22997755563','recrutamentoeselecao@hardyn.com.br','2022-08-19 18:06:44.019651',5,1,1,0,0,'','22997755563',1),(81,'Delícias da Serra','41180583000167','Rua Gertrudes Stern, 21 Debossan','24999246011','','2022-08-19 18:19:52.963014',5,1,0,0,0,'','24999246011',1),(82,'Superpão','05951912000162','Praça Marcílio Dias, 63 Paissandu','2225251550','rh3@superpao.com','2022-08-23 14:59:39.571536',5,1,1,1,0,'','',0),(83,'Gigalink','09257919000130','Av. Dr. Galdino do Vale Filho, 29 - loja A','22920188939','rh@gigalink.net.br','2022-08-23 15:02:43.817983',5,1,1,1,0,'','22920188939',1),(84,'Frilar Móveis','32550097000100','Av. Dr Galdino do Valle Filho, 3A 74 - Ao lado do xadrez','2225224300','a.gazoni@hotmail.com.br','2022-08-23 15:30:19.368775',5,1,1,1,0,'','22988370640',1),(85,'Sousa e Couto Assessoria Contábil e Financeira','10621721000172','Av. Galdino do Vale Filho, Centro','2225249000','rh@sousaecouto.com.br','2022-08-23 15:31:48.427555',5,1,1,0,0,'','22997652298',1),(86,'LacaLab - Laboratório das Águas','04272768000175','Rua Dr Julio Zamith, 21 - Centro','','comercial@lacalab.com.br','2022-08-27 18:31:08.760110',5,1,1,0,0,'','',0),(87,'Time Express','01515934000129','Rua Maximiliano Falck, 380 Ypú','2225256000','andre.a@timeexpress.com.br','2022-08-27 18:47:32.503798',5,1,1,1,0,'','',0),(88,'Boutique da Lou','41924797000109','Av. Alberto Braune N° 55','22997571820','','2022-08-27 18:51:47.621906',5,1,0,1,0,'','22997571820',1),(89,'Escola Técnica Santa Terezinha','13650362000170','Rua Antonio Goncalves Ribeiro, 634 - Cordeiro','22981336108','','2022-08-27 18:57:54.320610',5,1,0,0,1,'','22981336108',0),(90,'MR Costa Pimentel','34264992000186','Rua Presidente Vargas, Olaria','','selecaoestagio2019@hotmail.com','2022-08-27 19:00:44.219079',5,1,1,0,0,'','',0),(91,'Salão Linda Hair','32163694000174','Rua José Alberto Knust - Conselheiro','22997786942','','2022-08-27 19:10:09.568595',5,1,0,0,0,'','22997786942',1),(92,'Faol','30538060000123','Av. Governador Roberto Silveira, 3612 - Conselheiro','2225339900','','2022-08-27 19:13:24.619228',5,1,0,1,1,'Entregar currículo direto no local - De 08h às 11h de Terça à Quinta (Com CNH, CTPS, Currículo, comprovante de residência e foto 3x4)','',0),(93,'Multi Metais','06821350000103','Rua Antenor Francisco Brantes, 11 C - Córrego D’antas','2225271908','rh@multimetais.ind.br','2022-08-27 19:14:47.095557',5,1,1,0,0,'','',0),(94,'Juliarte','31172422000178','Rua Moisés Amélio, 56 Centro','2225233140','','2022-08-27 19:16:21.366930',5,1,0,1,0,'','',0),(95,'Martins Atacadista','18485037000112','Duque de Caxias','84981864851','mayara.silva@martins.com.br','2022-08-27 19:18:55.418068',5,1,1,0,0,'Mayara - Whatsapp','84981864851',1),(96,'Recurso Humanos 10','05516010000106','Av. Treze de Maio, 33 - Sala 2502','2122876988','','2022-08-27 19:21:11.435917',5,1,0,0,0,'','21969340248',1),(97,'Externato Serrano','26714898000153','Av. Campesina Friburguense, 110 Centro','2230664103','direcaoserrano@gmail.com','2022-08-27 19:28:01.169503',5,1,1,1,0,'','22981569195',1),(98,'Mazzini Adm e Empreitas','45517604000148','Rua Cardoso de Moraes N° 61 - Bonsucesso','2130427751','','2022-08-27 19:30:04.998307',5,1,0,0,0,'','21984894184',1),(99,'Valesca Marotti','34164547000144','Av. Dr. Galdino do Valle Filho, 23','22999917439','breno@valescamarotti.com.br','2022-08-27 19:33:31.305192',5,1,1,0,0,'','22999917439',1),(100,'Uelinton Garcia Reis','17157863000170','Rua Leuenroth 62 Paissandu','22992458188','','2022-08-27 19:38:07.471548',5,1,0,1,0,'','22992458188',1),(101,'AirFit Academia','39278407000110','Rua Moisés Amélio, 17 - loja 401 Centro','2220501600','curriculos.airfit@gmail.com','2022-08-27 19:40:57.593451',5,1,1,1,0,'','22997453899',1),(102,'General Contractor','73509440000142','Barra da Tijuca','2130309569','comercial@generalcontractor.com.br','2022-08-27 19:43:21.348140',5,1,1,0,0,'','',0),(103,'Banquete Auto Mecânica','31569734000110','Rodovia RJ 116 Km 97 Banquete','2225651191','banqueteautomecanica@yahoo.com.br','2022-08-27 19:46:37.483289',5,1,1,0,0,'','22981114764',1),(104,'Svoboda Telecomunicações','12657470000101','Macaé RJ','22999476136','rh@svoboda.com.br','2022-08-27 19:49:45.815231',5,1,1,0,0,'','22999476136',1),(105,'HAF Empreendimentos','23608728000104','São José de Ribamar/MA','98988819931','empreendimentos.haf@gmail.com','2022-08-27 19:54:34.529817',5,1,1,0,0,'','98988819931',1),(106,'Nova Clínica','21743615000188','Av. Alberto Braune, 12 - 7° andar','21969721398','thiagotrott@gmail.com','2022-08-27 19:59:09.226104',5,1,1,1,0,'','21969721398',1),(107,'PAF','08307536000166','Rua Lopes Trovão, 31 - Centro','22999613896','','2022-08-27 20:01:28.441841',5,1,0,1,0,'','',0),(108,'FriStar Comercial','32078016000103','Rua Raul Veiga, 200 Olaria','2225232347','compras@fristarcomercialtextil.com.br','2022-08-27 20:03:40.687619',5,1,1,0,0,'','',0),(109,'Luzitana Diversidade','07896696000125','Rua Moisés Amélio 18 - Centro','2225221739','','2022-08-27 20:08:33.058489',5,1,0,1,0,'','',0),(110,'Varejão dos Tecidos','23236489000109','Rua Moisés Amélio, 10 - Centro','2225238811','','2022-08-29 14:06:37.241689',5,1,0,1,1,'','',0),(111,'Agroponto Rações','05129345000163','Av. Governador Roberto Silveira, 924 - Jardim Ouro Preto','22992015033','gracar051@gmail.com','2022-08-29 14:08:27.129390',5,1,1,1,0,'','22992015033',1)
        ]

    for i in empresas:
        empresa=Empresa(nome=i[1], cnpj=i[2], endereco=i[3], telefone=i[4], whatsapp=i[13], email=i[5], ocultar=i[8], contato_presencial=i[9], contato_email=i[10], contato_telefone=i[11], contato_whatsapp=i[14], observacao=i[12], user=request.user, dt_inclusao=i[7])
        empresa.save()

    return redirect('/')
@login_required
def sair(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('vagas:home')
    else:
        return redirect('/accounts/login')