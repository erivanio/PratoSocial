# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=tagging.fields.TagField(default=None, help_text=b'palavras chaves separadas por v\xc3\xadrgula', max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
