# Generated by Django 2.1 on 2018-09-08 10:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0011_auto_20180907_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_id',
            field=models.CharField(default=uuid.UUID('f561fd91-670b-45a3-9acf-f3bccbca01c5'), max_length=200, primary_key=True, serialize=False),
        ),
    ]