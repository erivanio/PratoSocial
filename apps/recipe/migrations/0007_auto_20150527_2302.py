# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20150520_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name=b'photo_162x150',
            field=image_cropping.fields.ImageRatioField(b'photo', '162x150', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 162x150'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name=b'photo_235x151',
            field=image_cropping.fields.ImageRatioField(b'photo', '235x151', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 235x151'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name=b'photo_260x140',
            field=image_cropping.fields.ImageRatioField(b'photo', '260x140', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 260x140'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name=b'photo_260x300',
            field=image_cropping.fields.ImageRatioField(b'photo', '260x300', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 260x300'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name=b'photo_360x300',
            field=image_cropping.fields.ImageRatioField(b'photo', '360x300', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 360x300'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name=b'photo_560x290',
            field=image_cropping.fields.ImageRatioField(b'photo', '560x290', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo 560x290'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=None, max_length=150, blank=True),
            preserve_default=False,
        ),
    ]
