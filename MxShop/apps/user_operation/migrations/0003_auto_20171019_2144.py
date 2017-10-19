# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0002_auto_20171017_2017'),
        ('user_operation', '0002_auto_20171009_2140'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together=set([('user', 'goods')]),
        ),
    ]
