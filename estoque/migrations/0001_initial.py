# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 12:54
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('nome_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome')),
                ('descrição', models.TextField(blank=True, null=True)),
                ('valor_unit', models.FloatField(verbose_name='Valor Unitario')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentacaoEstoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('fluxo', models.BooleanField(choices=[(True, 'Entrada'), (False, 'Saida')])),
                ('data_informada', models.DateField()),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Item')),
                ('usuario_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]