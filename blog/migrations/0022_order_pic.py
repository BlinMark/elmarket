# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170429_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pic',
            field=models.ImageField(upload_to='', help_text='150x150px', blank=True, verbose_name='LOL'),
        ),
    ]
