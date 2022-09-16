# Generated by Django 4.1.1 on 2022-09-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='colors',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='team',
            name='era',
            field=models.CharField(default='Heisei', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='Test Sentai Testranger', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='series_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='year',
            field=models.IntegerField(default=1964),
            preserve_default=False,
        ),
    ]