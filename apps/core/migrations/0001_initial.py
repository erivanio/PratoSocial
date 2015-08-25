# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'Email', db_index=True)),
                ('username', models.CharField(unique=True, max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Ativo?')),
                ('is_member', models.BooleanField(default=True, verbose_name=b'Membro?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name=b'Administrador?')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Criado em')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=(models.Model,),
        ),
    ]
