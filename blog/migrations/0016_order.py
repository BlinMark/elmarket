# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170423_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Имя', null=True, blank=True)),
                ('sername', models.CharField(max_length=20, verbose_name='Фамилия', null=True, blank=True)),
                ('phone', models.PositiveIntegerField(verbose_name='Телефон', null=True, blank=True)),
                ('email', models.EmailField(max_length=30, verbose_name='E-mail', null=True, blank=True)),
                ('product_format', models.CharField(choices=[('Картина', 'Картина'), ('Постер', 'Постер')], default=0, verbose_name='Формат', max_length=50)),
                ('product_size', models.CharField(choices=[('A0 80*120 см. (80 р.)', 'A0 80*120 см. (80 р.)'), ('A1 60*80 см. (70 р.)', 'A1 60*80 см. (70 р.)'), ('A2 40*60 см. (60 р.)', 'A2 40*60 см. (60 р.)'), ('A3 30*40 см (50 р.)', 'A3 30*40 см (50 р.)'), ('A4 20*30 см. (40 р.)', 'A4 20*30 см. (40 р.)')], default=2, verbose_name='Размер', max_length=50)),
                ('product_orientation', models.CharField(choices=[('Горизонтальная', 'Горизонтальная'), ('Вертикальная', 'Вертикальная')], default=0, verbose_name='Ориентация', max_length=50)),
                ('product_kreplenie', models.CharField(choices=[('Клейкая лента (1 р.)', 'Клейкая лента (1 р.)'), ('Липучки нарезные (2 р.)', 'Липучки нарезные (2 р.)'), ('Липучки готовые (5 р.)', 'Липучки готовые (5 р.)'), ('Верёка + крючёк (7 р.)', 'Верёка + крючёк (7 р.)')], default=0, verbose_name='Способ крепления', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
    ]
