# Generated by Django 5.0.4 on 2024-05-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_imgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imgid',
            field=models.IntegerField(),
        ),
    ]
