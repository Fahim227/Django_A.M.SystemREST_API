# Generated by Django 3.1.7 on 2021-05-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_myimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myimage',
            name='model_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
