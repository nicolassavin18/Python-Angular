# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 17:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0007_auto_20160526_1725'),
        ('userprofile', '0002_auto_20160526_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=64, unique=True)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmation_emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoginMagicLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=64, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magic_links', to='company.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magic_links', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]