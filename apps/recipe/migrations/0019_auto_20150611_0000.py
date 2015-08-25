# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0018_auto_20150609_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default=None, upload_to=b'uploads/receitas/', verbose_name=b'Foto'),
            preserve_default=False,
        ),
    ]
