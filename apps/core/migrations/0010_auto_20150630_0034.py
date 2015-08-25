# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Estado', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'AM', b'Amazonas'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maran\xc3\xa3o'), (b'MT', b'Mato Grosso'), (b'MS', b'Mato Grosso do Sul'), (b'MG', b'Minas Gerais'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PR', b'Paran\xc3\xa1'), (b'PE', b'Pernanbuco'), (b'PI', b'Piau\xc3\xad'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RS', b'Rio Grande do Sul'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'SC', b'Santa Catarina'), (b'SP', b'S\xc3\xa3o Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=apps.core.models.update_filename, null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
