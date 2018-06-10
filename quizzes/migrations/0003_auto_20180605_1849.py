# Generated by Django 2.0.5 on 2018-06-05 18:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20180605_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular answer across whole library', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='answers',
            field=models.ManyToManyField(help_text='Select answers for the question', to='quizzes.Answer'),
        ),
    ]
