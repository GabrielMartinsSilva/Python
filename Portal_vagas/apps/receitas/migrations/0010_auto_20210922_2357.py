# Generated by Django 2.2.6 on 2021-09-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0009_auto_20210922_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='descricao',
            field=models.TextField(),
        ),
    ]