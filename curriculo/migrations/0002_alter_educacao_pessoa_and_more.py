# Generated by Django 4.2.2 on 2023-08-01 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_pessoa_objetivo'),
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educacao',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa'),
        ),
        migrations.AlterField(
            model_name='experienciaprofissional',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa'),
        ),
    ]
