# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='snapwidget',
            field=models.TextField(help_text=b'Adicione o c\xc3\xb3digo gerado pelo site http://snapwidget.com', null=True, blank=True),
            preserve_default=True,
        ),
    ]
