# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_user_recipe_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name=b'photo_thumb',
            field=image_cropping.fields.ImageRatioField(b'photo', '65x65', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo thumb'),
            preserve_default=False,
        ),
    ]
