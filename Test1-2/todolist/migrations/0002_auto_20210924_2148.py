# Generated by Django 3.2.7 on 2021-09-24 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='post',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='date_publish',
            new_name='cre_dtm',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='header',
        ),
    ]
