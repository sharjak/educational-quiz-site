# Generated by Django 2.0.5 on 2018-06-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_auto_20180605_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
