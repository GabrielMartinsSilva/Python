# Generated by Django 2.2.6 on 2021-08-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='nome_receita',
            field=models.CharField(max_length=248),
        ),
    ]
