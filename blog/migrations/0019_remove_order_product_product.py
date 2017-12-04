# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170425_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_product',
        ),
    ]
