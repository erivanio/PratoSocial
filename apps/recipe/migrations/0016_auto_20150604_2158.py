# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_commentwithpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentwithpic',
            name=b'image_thumb',
            field=image_cropping.fields.ImageRatioField(b'image', '135x100', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='image thumb'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentwithpic',
            name='image',
            field=models.ImageField(null=True, upload_to=b'uploads/comments/%Y/%m/%d/', blank=True),
            preserve_default=True,
        ),
    ]
