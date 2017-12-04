# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_order_product_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.CharField(null=True, max_length=100, verbose_name='Товар', blank=True),
        ),
    ]
