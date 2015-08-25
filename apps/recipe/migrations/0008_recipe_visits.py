# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20150527_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='visits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
