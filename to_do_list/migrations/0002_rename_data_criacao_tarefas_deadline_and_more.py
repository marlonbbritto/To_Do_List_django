# Generated by Django 5.0.1 on 2024-02-18 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefas',
            old_name='data_criacao',
            new_name='deadline',
        ),
        migrations.RenameField(
            model_name='tarefas',
            old_name='concluida',
            new_name='done',
        ),
        migrations.RenameField(
            model_name='tarefas',
            old_name='tarefa',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='tarefas',
            old_name='usuario',
            new_name='user',
        ),
    ]