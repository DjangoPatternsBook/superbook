# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Ordinary'), (1, 'SuperHero')], max_length=1, null=True),
            preserve_default=True,
        ),
    ]
