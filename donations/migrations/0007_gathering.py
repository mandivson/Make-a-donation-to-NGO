# Generated by Django 3.1.2 on 2020-10-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gathering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name5', models.CharField(max_length=30)),
                ('place5', models.CharField(max_length=30)),
                ('cause5', models.CharField(max_length=30)),
                ('date5', models.DateField(max_length=30)),
                ('time5', models.TimeField(max_length=30)),
            ],
        ),
    ]
