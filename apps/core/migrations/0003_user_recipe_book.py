# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
        ('core', '0002_auto_20150505_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recipe_book',
            field=models.ManyToManyField(related_name='recipe_user', null=True, to='recipe.Recipe', blank=True),
            preserve_default=True,
        ),
    ]
