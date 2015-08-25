# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_slide_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
    ]
