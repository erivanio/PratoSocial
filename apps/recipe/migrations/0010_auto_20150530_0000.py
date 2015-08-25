# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_recipe_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=None, verbose_name=b'Ingredientes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='method_of_preparation',
            field=models.TextField(default=None, verbose_name=b'Modo de preparo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='produce',
            field=models.CharField(default=None, max_length=20, verbose_name=b'Redimento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_of_preparation',
            field=models.CharField(default=None, max_length=20, verbose_name=b'Tempo de preparo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(help_text=b'Breve descri\xc3\xa7\xc3\xa3o da receita', verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
    ]
