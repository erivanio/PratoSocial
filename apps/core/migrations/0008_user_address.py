# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_photo_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=90, null=True, verbose_name=b'Endere\xc3\xa7o', blank=True),
            preserve_default=True,
        ),
    ]
