# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_order_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_kreplenie',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_orientation',
        ),
    ]
