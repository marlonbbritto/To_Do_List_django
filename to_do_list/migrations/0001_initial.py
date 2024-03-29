# Generated by Django 5.0.1 on 2024-01-25 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('tarefa', models.CharField(max_length=100)),
                ('data_criacao', models.DateField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=True)),
                ('concluida', models.BooleanField(default=False)),
                ('data_atualizacao_concluida', models.DateField()),
            ],
        ),
    ]
