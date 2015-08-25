# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_auto_20150530_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name=b'photo_350x350',
            field=image_cropping.fields.ImageRatioField(b'photo', '350x350', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 350x350'),
            preserve_default=False,
        ),
    ]
