# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(to='store.Attribute', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='store.Image', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pricing',
            field=models.ManyToManyField(to='store.Price', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(max_digits=15, decimal_places=7, blank=True),
        ),
    ]
