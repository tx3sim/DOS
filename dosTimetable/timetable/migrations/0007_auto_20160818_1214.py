# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_remove_class_levelname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LevelModule',
            new_name='classModule',
        ),
        migrations.RenameModel(
            old_name='ClassLevel',
            new_name='Course',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='types',
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]
