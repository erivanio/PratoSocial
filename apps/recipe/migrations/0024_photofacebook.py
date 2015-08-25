# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.recipe.models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0023_recipe_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoFacebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=apps.recipe.models.update_filename, verbose_name=b'Foto Facebook', blank=True)),
                ('image_url', models.URLField()),
                (b'photo_thumb', image_cropping.fields.ImageRatioField(b'image_file', '135x100', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo thumb')),
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
