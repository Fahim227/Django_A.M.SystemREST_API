# Generated by Django 3.1.7 on 2021-04-09 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='todo_practice',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
