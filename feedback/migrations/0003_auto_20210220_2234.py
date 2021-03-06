# Generated by Django 3.1.6 on 2021-02-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20210220_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='approachability',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='class_control',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='practical_knowlegde',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='punctuality',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='competency',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='teachings_skills',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
    ]
