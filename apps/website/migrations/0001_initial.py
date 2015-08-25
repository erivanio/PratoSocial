# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_recipe_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(help_text=b'Imagem para o slide da p\xc3\xa1gina inicial, tamanho 1200x400', upload_to=b'uploads/slide/', verbose_name=b'Foto')),
                ('status', models.BooleanField(default=True, verbose_name=b'Ativo?')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data do Cadastro', blank=True)),
                ('recipe', models.ForeignKey(blank=True, to='recipe.Recipe', help_text=b'Para associar uma receita ao slide.', null=True, verbose_name=b'Receita')),
            ],
            options={
                'ordering': ('created_at',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('instagram', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('youtube', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Rede Social',
                'verbose_name_plural': 'Redes Sociais',
            },
            bases=(models.Model,),
        ),
    ]
