# Generated by Django 3.1.2 on 2020-11-02 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.IntegerField()),
                ('modelo', models.CharField(max_length=25)),
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
                ('unidadereferente', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoEstoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidadeProdutoReferente', models.IntegerField()),
                ('produtoReferente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtoReferente', to='produto.produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='tipoDeItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipodeitem', to='produto.tipoitemproduto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidade', to='produto.unidadeproduto'),
        ),
    ]