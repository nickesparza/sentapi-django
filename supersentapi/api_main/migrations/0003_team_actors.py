# Generated by Django 4.1.1 on 2022-09-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0002_team_colors_team_era_team_name_team_series_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='actors',
            field=models.JSONField(default=dict),
        ),
    ]
