# Generated by Django 2.1 on 2020-01-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('date_recieved', models.CharField(max_length=100)),
                ('student_roll_number', models.CharField(max_length=255)),
            ],
        ),
    ]
