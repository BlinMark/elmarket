# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_product_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(verbose_name='Размер', default='A1', choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5')], max_length=2),
        ),
    ]
