# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo_url',
            field=models.URLField(blank=True, default=None, max_length=250, null=True, verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='person',
            name='prefix',
            field=models.CharField(blank=True, choices=[('PHD', 'PhD.'), ('MSC', 'MSc.'), ('ENG', 'Ing.'), ('MAL', 'Sr.'), ('FEM', 'Sra.')], default=None, max_length=3, null=True, verbose_name='Prefijo'),
        ),
    ]