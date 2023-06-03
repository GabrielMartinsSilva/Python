# Generated by Django 2.2.6 on 2021-09-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_auto_20210819_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='ingredientes',
            new_name='competencia',
        ),
        migrations.RenameField(
            model_name='receita',
            old_name='modo_preparo',
            new_name='competencia2',
        ),
        migrations.RenameField(
            model_name='receita',
            old_name='date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='receita',
            old_name='titulo_vaga',
            new_name='titulo_vaga',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='foto_receita',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='rendimento',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='tempo_preparo',
        ),
        migrations.AddField(
            model_name='receita',
            name='curso',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receita',
            name='localizacao',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
