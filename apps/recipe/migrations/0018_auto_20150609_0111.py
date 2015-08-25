# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0017_recipebook_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name=b'photo_350x350',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name=b'photo_360x300',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name=b'photo_560x290',
        ),
        migrations.AddField(
            model_name='recipe',
            name=b'photo_450x450',
            field=image_cropping.fields.ImageRatioField(b'photo', '450x450', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 450x450'),
            preserve_default=False,
        ),
    ]
