# Generated by Django 2.0.5 on 2018-06-05 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20180605_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='name',
            new_name='title',
        ),
    ]