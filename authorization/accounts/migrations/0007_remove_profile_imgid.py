# Generated by Django 5.0.4 on 2024-05-01 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_imgid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='imgid',
        ),
    ]
