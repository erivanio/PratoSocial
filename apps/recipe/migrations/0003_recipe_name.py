# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default=None, max_length=100, verbose_name=b'Nome'),
            preserve_default=False,
        ),
    ]
