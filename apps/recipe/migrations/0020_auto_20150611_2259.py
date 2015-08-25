# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0019_auto_20150611_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentwithpic',
            options={'verbose_name': 'Coment\xe1rio', 'verbose_name_plural': 'Coment\xe1rios'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='sugestion_day',
            field=models.BooleanField(default=False, verbose_name=b'Sugest\xc3\xa3o do dia'),
            preserve_default=True,
        ),
    ]
