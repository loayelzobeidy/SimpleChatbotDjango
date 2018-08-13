# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-12 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('employed', models.BooleanField()),
                ('job_title', models.CharField(max_length=200)),
                ('years_of_experience', models.IntegerField()),
                ('seeking_titles', models.ManyToManyField(to='chats.Title')),
                ('skills', models.ManyToManyField(to='chats.Skill')),
            ],
        ),
    ]
