# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text=b'Ingredientes e modo de preparo', verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('photo', models.ImageField(upload_to=b'uploads/user/', null=True, verbose_name=b'Foto', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
            bases=(models.Model,),
        ),
    ]
