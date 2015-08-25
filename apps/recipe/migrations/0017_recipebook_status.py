# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0016_auto_20150604_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipebook',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
