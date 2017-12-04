# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_product',
            field=models.CharField(verbose_name='Товар', max_length=100, default=blog.models.Product),
        ),
    ]
