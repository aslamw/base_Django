# Generated by Django 4.1 on 2022-08-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_data_criacao_alter_evento_data_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do Evento'),
        ),
    ]
