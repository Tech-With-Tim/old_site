# Generated by Django 3.2.3 on 2021-07-05 22:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timathon', '0014_alter_submission_repl_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='c1',
            field=models.IntegerField(default=1, help_text='Criterion 1', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='vote',
            name='c2',
            field=models.IntegerField(default=1, help_text='Criterion 2', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='vote',
            name='c3',
            field=models.IntegerField(default=1, help_text='Criterion 3', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='vote',
            name='c4',
            field=models.IntegerField(default=1, help_text='Criterion 4', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='vote',
            name='notes',
            field=models.TextField(blank=True, help_text='Extra notes', max_length=2048, null=True),
        ),
    ]
