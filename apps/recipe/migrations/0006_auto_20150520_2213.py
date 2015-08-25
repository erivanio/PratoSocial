# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20150520_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipebook',
            old_name='student',
            new_name='user',
        ),
    ]
