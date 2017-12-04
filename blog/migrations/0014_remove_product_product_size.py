# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_product_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_size',
        ),
    ]
