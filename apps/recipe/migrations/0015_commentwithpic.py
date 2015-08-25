# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '__first__'),
        ('recipe', '0014_recipebook_photo_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentWithPic',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_comments.Comment')),
                ('image', models.ImageField(null=True, upload_to=b'comments/%Y/%m/%d/', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_comments.comment',),
        ),
    ]
