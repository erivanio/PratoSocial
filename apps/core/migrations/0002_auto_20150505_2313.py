# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default=None, help_text=b'Deve conter no m\xc3\xa1ximo 140 caracteres', unique=True, max_length=140, verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=b'uploads/user/', null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
