# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20140829_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_url',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]
