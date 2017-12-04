# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170313_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.PositiveIntegerField(default='2017', verbose_name='Год'),
        ),
    ]
