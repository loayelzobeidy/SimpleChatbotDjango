# Generated by Django 2.1 on 2018-09-05 22:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20180905_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_id',
            field=models.CharField(default=uuid.UUID('9611e059-a5ef-4bb8-942d-020c94985b6a'), max_length=200, primary_key=True, serialize=False),
        ),
    ]
