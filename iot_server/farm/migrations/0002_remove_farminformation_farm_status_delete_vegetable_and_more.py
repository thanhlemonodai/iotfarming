# Generated by Django 4.0.4 on 2022-05-27 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farminformation',
            name='farm_status',
        ),
        migrations.DeleteModel(
            name='Vegetable',
        ),
        migrations.DeleteModel(
            name='FarmInformation',
        ),
        migrations.DeleteModel(
            name='FarmStatus',
        ),
    ]