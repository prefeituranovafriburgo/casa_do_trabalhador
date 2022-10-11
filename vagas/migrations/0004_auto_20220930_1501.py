# Generated by Django 3.1.4 on 2022-09-30 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vagas', '0003_alter_empresa_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='cpf',
            field=models.CharField(default='', max_length=14, verbose_name='CPF do candidato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidato',
            name='funcionario_encaminhamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vaga_emprego',
            name='dt_desativacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Dt. Desativação'),
        ),
        migrations.AlterField(
            model_name='vaga_emprego',
            name='tipo_de_vaga',
            field=models.CharField(choices=[('NML', 'Padrão'), ('JAP', 'Jovem aprendiz'), ('PED', 'Pessoa com deficiência'), ('EST', 'Estágio')], default='NML', max_length=3),
        ),
    ]
