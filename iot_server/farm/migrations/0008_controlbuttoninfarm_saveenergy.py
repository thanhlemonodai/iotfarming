# Generated by Django 4.0.6 on 2022-10-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0007_controlbuttoninfarm'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlbuttoninfarm',
            name='saveEnergy',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
