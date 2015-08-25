# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.recipe.models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0021_photoinstagram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
        migrations.AlterField(
            model_name='commentwithpic',
            name='image',
            field=models.ImageField(null=True, upload_to=apps.recipe.models.update_filename, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoinstagram',
            name='image_file',
            field=models.ImageField(upload_to=apps.recipe.models.update_filename, verbose_name=b'Foto Instagram', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoinstagram',
            name=b'photo_thumb',
            field=image_cropping.fields.ImageRatioField(b'image_file', '135x100', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo thumb'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photorecipe',
            name='photo',
            field=models.ImageField(upload_to=apps.recipe.models.update_filename, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=apps.recipe.models.update_filename, verbose_name=b'Foto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipebook',
            name='photo',
            field=models.ImageField(upload_to=apps.recipe.models.update_filename, null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
