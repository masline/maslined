# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('parent', models.ForeignKey(to='store.Attribute', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50, verbose_name='Description of Image', blank=True)),
                ('picture', models.ImageField(upload_to='imgs/full', db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50, verbose_name='Description of Logo', blank=True)),
                ('picture', models.ImageField(upload_to='imgs/logo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('home_page', models.URLField(blank=True)),
                ('is_linecard', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True)),
                ('logo', models.ForeignKey(to='store.Logo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('price', models.DecimalField(max_digits=15, decimal_places=7)),
                ('min_qty', models.PositiveIntegerField()),
                ('max_qty', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('item_no', models.CharField(max_length=50, verbose_name='The manufacturer supplied part number', db_index=True)),
                ('weight', models.DecimalField(max_digits=15, decimal_places=7)),
                ('attributes', models.ManyToManyField(to='store.Attribute')),
                ('images', models.ManyToManyField(to='store.Image')),
                ('manu_no', models.ForeignKey(to='store.Manufacturer')),
                ('pricing', models.ManyToManyField(to='store.Price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
