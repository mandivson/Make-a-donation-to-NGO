# Generated by Django 3.1.2 on 2020-10-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_auto_20201005_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30)),
                ('username1', models.CharField(max_length=30, unique=True)),
                ('email1', models.EmailField(max_length=30)),
                ('password1', models.CharField(max_length=30)),
                ('district1', models.CharField(max_length=30)),
            ],
        ),
    ]
