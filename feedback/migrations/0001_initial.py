# Generated by Django 3.1.6 on 2021-02-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('competency', models.CharField(max_length=200)),
                ('teachings_skills', models.CharField(max_length=200)),
            ],
        ),
    ]
