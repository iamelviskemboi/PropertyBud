# Generated by Django 3.0.6 on 2020-05-21 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200521_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]