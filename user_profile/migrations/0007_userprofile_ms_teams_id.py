# Generated by Django 3.2.7 on 2021-09-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20210913_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ms_teams_id',
            field=models.EmailField(default='', max_length=254, verbose_name='MS Teams ID'),
        ),
    ]
