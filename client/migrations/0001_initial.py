# Generated by Django 3.1.2 on 2020-11-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('cpf', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=8)),
                ('ddd', models.IntegerField()),
                ('telefone', models.IntegerField()),
            ],
        ),
    ]
