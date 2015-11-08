# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(max_length=500)),
                ('privacy', models.CharField(max_length=12, choices=[('public', 'Public'), ('individual', 'Individual')], default='public')),
                ('posted_by', models.ForeignKey(null=True, related_name='posts', blank=True, to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(null=True, related_name='recieved_posts', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(to='posts.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.ForeignKey(null=True, related_name='comments', blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
