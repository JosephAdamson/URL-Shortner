# Generated by Django 4.0.6 on 2022-07-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='has_alias',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
