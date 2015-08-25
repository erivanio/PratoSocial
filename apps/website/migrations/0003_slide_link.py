# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_socialnetwork_snapwidget'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='link',
            field=models.URLField(help_text=b'Para redirecionar a outra p\xc3\xa1gina.', null=True, blank=True),
            preserve_default=True,
        ),
    ]
