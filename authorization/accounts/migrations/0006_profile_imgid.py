# Generated by Django 5.0.4 on 2024-05-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='imgid',
            field=models.IntegerField(default=1),
        ),
    ]
