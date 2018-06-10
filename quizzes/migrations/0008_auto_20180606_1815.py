# Generated by Django 2.0.5 on 2018-06-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_auto_20180606_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='theme',
        ),
        migrations.AddField(
            model_name='quiz',
            name='theme',
            field=models.ForeignKey(default='default theme', on_delete=django.db.models.deletion.CASCADE, to='quizzes.Theme'),
        ),
    ]
