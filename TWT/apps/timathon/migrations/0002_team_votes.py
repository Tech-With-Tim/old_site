# Generated by Django 3.1.1 on 2020-09-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
