# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor_uploader.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=datetime.datetime(2017, 11, 2, 17, 58, 36, 918411, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
