# Generated by Django 3.1.7 on 2021-05-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20210430_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='none/no-img.jpg', upload_to='images/')),
            ],
        ),
    ]