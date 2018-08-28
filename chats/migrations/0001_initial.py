# Generated by Django 2.1 on 2018-08-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('skill',),
            },
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
                ('employed', models.BooleanField(default=False)),
                ('job_title', models.CharField(max_length=200)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('seeking_titles', models.ManyToManyField(to='chats.Title')),
                ('skills', models.ManyToManyField(to='chats.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.OneToOneField(on_delete=None, to='chats.User'),
        ),
    ]
