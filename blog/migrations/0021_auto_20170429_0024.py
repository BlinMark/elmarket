# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.CharField(max_length=100, blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_size',
            field=models.CharField(max_length=50, choices=[('A1 (60*80 см)', 'A1 (60*80 см)'), ('A2 (40*60 см)', 'A2 (40*60 см)'), ('A3 (30*40 см)', 'A3 (30*40 см)')], default=2, verbose_name='Размер'),
        ),
    ]
