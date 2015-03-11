# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantDate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-date',),
            },
            bases=(models.Model,),
        ),
    ]
