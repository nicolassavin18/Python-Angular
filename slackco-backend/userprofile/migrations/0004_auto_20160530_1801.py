# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_emailconfirmation_loginmagiclink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailconfirmation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='loginmagiclink',
            name='user',
        ),
        migrations.AddField(
            model_name='emailconfirmation',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='confirmation_emails', to='userprofile.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loginmagiclink',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='magic_links', to='userprofile.UserProfile'),
            preserve_default=False,
        ),
    ]
