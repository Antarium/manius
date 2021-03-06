# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-31 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(verbose_name='Денег на счету'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='account',
            name='target',
            field=models.CharField(default='Не указано', max_length=50, verbose_name='цель изменения счета'),
        ),
    ]
