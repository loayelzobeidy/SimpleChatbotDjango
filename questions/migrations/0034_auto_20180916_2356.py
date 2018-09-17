# Generated by Django 2.1 on 2018-09-16 23:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0033_auto_20180914_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possibleanswer',
            name='answer_id',
            field=models.CharField(default=uuid.UUID('7a913907-11f4-4634-9959-7278f6f693d1'), max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(default=uuid.UUID('f3ef88ba-3561-44a8-b66d-900313d11e64'), max_length=200, primary_key=True, serialize=False),
        ),
    ]
