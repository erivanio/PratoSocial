# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150519_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(help_text=b'Deve conter no m\xc3\xa1ximo 140 caracteres', max_length=140, null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
    ]
