# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_recipe_photo_350x350'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'uploads/receitas/%Y/%m/', verbose_name=b'Foto', blank=True)),
                (b'photo_thumb', image_cropping.fields.ImageRatioField(b'photo', '135x100', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo thumb')),
                ('recipe', models.ForeignKey(verbose_name=b'Receita', to='recipe.Recipe')),
            ],
            options={
                'ordering': ['recipe'],
                'verbose_name': 'Foto de Receita',
                'verbose_name_plural': 'Fotos de Receitas',
            },
            bases=(models.Model,),
        ),
    ]
