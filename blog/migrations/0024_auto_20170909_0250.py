# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20170429_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AlterField(
            model_name='order',
            name='product_size',
            field=models.CharField(choices=[('A1 (60*80 см)', 'A1 (60*80 см)'), ('A2 (40*60 см)', 'A2 (40*60 см)'), ('A3 (30*40 см)', 'A3 (30*40 см)')], default='A3 (30*40 см)', verbose_name='Размер', max_length=50),
        ),
    ]
