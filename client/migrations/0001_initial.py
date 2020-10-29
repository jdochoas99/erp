# Generated by Django 3.1.2 on 2020-10-29 14:27

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='tipoItemProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDeItem', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='unidadeProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.IntegerField()),
                ('modelo', models.CharField(max_length=25)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('precovendaVarejo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('precovendaAtacado', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipoDeItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipodeitem', to='client.tipoitemproduto')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidadeproduto', to='client.unidadeproduto')),
            ],
        ),
    ]
