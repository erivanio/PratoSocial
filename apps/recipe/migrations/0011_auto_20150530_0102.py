# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_auto_20150530_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipebook',
            name='description',
            field=models.TextField(help_text=b'Breve descri\xc3\xa7\xc3\xa3o da livro', null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipebook',
            name='photo',
            field=models.ImageField(upload_to=b'uploads/livro-receitas/', null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
