# Generated by Django 2.2.6 on 2021-09-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0008_auto_20210921_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='competencia2',
        ),
        migrations.AddField(
            model_name='receita',
            name='descricao',
            field=models.CharField(default='', max_length=248),
            preserve_default=False,
        ),
    ]