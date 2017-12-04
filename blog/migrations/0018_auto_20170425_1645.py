# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_order_product_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_product',
            field=models.CharField(max_length=100, verbose_name='Товар'),
        ),
    ]
