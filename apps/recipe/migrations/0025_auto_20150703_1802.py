# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0024_photofacebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=apps.recipe.models.update_filename, null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
