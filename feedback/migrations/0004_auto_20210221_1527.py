# Generated by Django 3.1.6 on 2021-02-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20210220_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='class_control',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='practical_knowlegde',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='teachings_skills',
        ),
        migrations.AddField(
            model_name='feedback',
            name='class_Control',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='practical_Knowlegde',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='teachings_Skills',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='approachability',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='competency',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='punctuality',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=True),
        ),
    ]