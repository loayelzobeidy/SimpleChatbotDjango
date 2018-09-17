# Generated by Django 2.1 on 2018-09-14 00:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0031_auto_20180914_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possibleanswer',
            name='answer_id',
            field=models.CharField(default=uuid.UUID('b7024d80-731b-4dd5-8f7b-89615bf872e1'), max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(default=uuid.UUID('6ee006c0-48d2-464f-abc9-09de8a87ec5c'), max_length=200, primary_key=True, serialize=False),
        ),
    ]