from django import template
from ..models import Candidato
register = template.Library()

@register.filter
def qntcandidatos(obj):       
    try:
        candidatos=Candidato.objects.filter(vaga=obj)
        return str(len(candidatos))
    except:
        return None

@register.filter
def mascarar_cpf(cpf):
    """Exibe apenas os 3 primeiros dígitos do CPF, mascarando o restante."""
    if not cpf:
        return ''
    digits = ''.join(c for c in str(cpf) if c.isdigit())
    if len(digits) >= 3:
        return digits[:3] + '.XXX.XXX-XX'
    return str(cpf)

@register.filter
def mascarar_cnpj(cnpj):
    """Exibe apenas os 3 primeiros dígitos do CNPJ, mascarando o restante."""
    if not cnpj:
        return ''
    digits = ''.join(c for c in str(cnpj) if c.isdigit())
    if len(digits) >= 3:
        return digits[:3].zfill(3) + '.XXX.XXX/XXXX-XX'
    return str(cnpj)
