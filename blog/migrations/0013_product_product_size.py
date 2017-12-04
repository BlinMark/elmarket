# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_product_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5')], default='A1', verbose_name='Размер', max_length=2),
        ),
    ]
