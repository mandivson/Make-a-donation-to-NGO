# Generated by Django 3.1.2 on 2020-10-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_auto_20201005_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name4', models.CharField(max_length=30)),
                ('mobile4', models.IntegerField(max_length=30)),
                ('address4', models.CharField(max_length=30)),
                ('date4', models.DateField(max_length=30)),
                ('time4', models.TimeField(max_length=30)),
            ],
        ),
    ]
