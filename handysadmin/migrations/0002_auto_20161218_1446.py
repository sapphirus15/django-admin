# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('handysadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=45)),
                ('user_nickname', models.CharField(max_length=45)),
                ('user_country_code', models.CharField(max_length=45)),
                ('user_phone', models.CharField(max_length=45)),
                ('user_kakaoid', models.CharField(max_length=45)),
                ('user_desc', models.TextField()),
                ('user_has_car', models.IntegerField()),
                ('user_available', models.IntegerField()),
                ('user_sendbird_token', models.CharField(max_length=45)),
                ('user_sendbird_token2', models.CharField(max_length=45)),
                ('user_sendbird_room', models.TextField()),
                ('user_hashkey', models.TextField()),
                ('user_is_del', models.IntegerField()),
                ('user_email', models.CharField(max_length=45)),
                ('user_status', models.IntegerField()),
                ('user_password', models.CharField(max_length=45)),
                ('user_memo', models.TextField()),
                ('user_created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserAreaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_area_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type_desc', models.CharField(max_length=45)),
                ('user_type_status', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_area',
            field=models.ForeignKey(to='handysadmin.UserAreaType'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type_id',
            field=models.ForeignKey(to='handysadmin.UserType'),
        ),
    ]
