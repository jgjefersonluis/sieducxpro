# Generated by Django 2.2.7 on 2019-11-07 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('idade', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=13)),
                ('responsavel', models.CharField(max_length=150)),
                ('pesquisador', models.CharField(max_length=100)),
                ('data_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
