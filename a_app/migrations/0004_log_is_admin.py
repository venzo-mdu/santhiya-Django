# Generated by Django 3.2.6 on 2022-05-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_app', '0003_rename_name_profile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]