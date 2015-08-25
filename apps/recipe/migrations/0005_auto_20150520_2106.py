# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0004_recipe_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nome')),
                ('recipes', models.ManyToManyField(to='recipe.Recipe', null=True, verbose_name=b'Receitas', blank=True)),
                ('student', models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Livro de receita',
                'verbose_name_plural': 'Livros de receitas',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=b'uploads/receitas/', null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
