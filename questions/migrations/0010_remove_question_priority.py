# Generated by Django 2.1 on 2018-08-31 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20180831_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='priority',
        ),
    ]
