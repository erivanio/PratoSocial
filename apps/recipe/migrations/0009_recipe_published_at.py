# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_recipe_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Publicacao'),
            preserve_default=True,
        ),
    ]
