# Generated by Django 2.1 on 2018-08-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20180831_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='priority',
            field=models.IntegerField(unique=True),
        ),
    ]