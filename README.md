# Casa do Trabalhador <br>


> <p>Através de seus serviços, a Casa do Trabalhador oferece diversas oportunidades de emprego, seja para aqueles que buscam uma colocação profissional ou para empresas que desejam contratar novos colaboradores.  <br>Além disso, o órgão também pode fornecer informações sobre direitos trabalhistas, programas de capacitação e formação profissional, bem como orientações para a elaboração de currículos e preparação para entrevistas de emprego. <br>A Casa do Trabalhador de Nova Friburgo atua como um importante elo entre empregadores e trabalhadores, contribuindo para o desenvolvimento econômico da região ao fomentar o emprego e a qualificação profissional da população. Seu compromisso é promover uma relação harmoniosa e justa entre o mercado de trabalho e os cidadãos, contribuindo para o fortalecimento do setor produtivo e o progresso da comunidade local.</p>


### Principais tecnologias
<p>
<img src="https://img.icons8.com/color/48/000000/python.png"/>&nbsp;&nbsp;
<img src="https://img.icons8.com/color/48/000000/django.png"/>&nbsp;&nbsp;
<img src="https://img.icons8.com/color/48/000000/bootstrap.png"/>&nbsp;&nbsp;
<img src="https://img.icons8.com/windows/48/000000/font-awesome.png"/>&nbsp;&nbsp;
<img src="https://img.icons8.com/color/48/000000/maria-db.png"/>
</p>

## 💻 Pré-requisitos
- Versão 3 ou mais recente de Python.
- MariaDB ou MySql (Algumas consultas foram otimizadas usando querys p/ MariaDB)




## 📦 Instalação de dependências

Para instalar as dependências do projeto basta usar o comando:<br>
`pip install -r requirements.txt`

Ou instale os módulos abaixo:

- asgiref==3.7.2
- beautifulsoup4==4.12.2
- certifi==2023.5.7
- charset-normalizer==3.1.0
- Django==4.2.2
- django-bootstrap-v5==1.0.11
- django-rest-framework==0.1.0
- django-widget-tweaks==1.4.12
- djangorestframework==3.14.0
- idna==3.4
- pdfkit==1.0.0
- PyMySQL==1.0.3
- python-dateutil==2.8.2
- pytz==2023.3
- PyYAML==6.0
- requests==2.31.0
- six==1.16.0
- soupsieve==2.4.1
- sqlparse==0.4.4
- tzdata==2023.3
- urllib3==2.0.3



## 🔧 Configurações
### Configurando as variáveis de ambiente.

Para criar as variáveis de ambiente crie um arquivo com o nome `.envvars.yaml` na raiz do seu projeto ou no diretório **acima da pasta do seu projeto** contendo as seguintes informações conforme o modelo abaixo:
```
db_host: '127.0.0.1'
db_name: 'nomedobanco' # Este projeto foi pensando para suportar MySql ou MariaDB
db_user: 'usuariodobanco' # Usuário do banco com todas as permissões para a base de dados
db_pw: 'senhadobanco' # A senha do respectivo usuário do banco
django_secret_key: 'secretkey123456' # Insira sua django secret key
debug_mode: True # Use True para DEBUG or False para PRODUCTION
sqlite_mode: True # Use True para usar a engine do SQLITE, mas faça isso apenas em desenvolvimento
email_sistema: 'seu@email.com' # E-mail utilizado para recuperação de senha
email_pw: 'su@senha123' # Senha do email acima
hCAPTCHA_Public_Key: '6484-dsadad4994ds9492314' # Inscreva-se https://www.hcaptcha.com/
hCAPTCHA_Secret_Key: '6484-dsadad4994ds94914dsd4900c0952' # Cadastre seu site após se inscrever
GOOGLE_OAUTH2_PUBLIC_KEY: '74526484-dsadad494d2314.apps.googleusercontent.com' # Inscreva-se https://console.cloud.google.com/ e gere as chaves para seu site
GOOGLE_OAUTH2_SECRET_KEY: 'GOCSPX-dsadad49das9494d2314'
FACEBOOK_DEVELOPER_PUBLIC_KEY: '4994ds949494d14' # Inscreva-se https://developers.facebook.com/ e gere as chaves para seu site
FACEBOOK_DEVELOPER_SECRET_KEY: '494d231479ff65cb6307b3'
```

------------


## Usando o projeto
Comece criando as tabelas do banco com o seguinte comando:
`python manage.py migrate` <br>
Para utilizar o projeto, você precisa criar um usuário utilizando o seguinte comando: <br>
`python manage.py createsuperuser`  <br>
No campo de usuário, você **deverá** informar o seu **e-mail**. As credenciais (e-mail e senha) serão utilizadas para realizar o login no site.