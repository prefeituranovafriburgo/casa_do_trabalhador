from django.urls import path
from . import views
app_name='cv'
urlpatterns = [
    path('curriculo', views.index, name='index'),
    path('curriculo/educacao', views.cadastrar_educacao, name='educacao'),
    path('curriculo/educacao/<id>/excluir', views.excluir_educacao, name='excluir_educacao'),
    path('curriculo/experiencia', views.cadastrar_experiencia, name='experiencia'),
     path('curriculo/experiencia/<id>/excluir', views.excluir_experiencia, name='excluir_experiencia'),
    path('curriculo/visualizar', views.curriculo, name='curriculo'), 

]