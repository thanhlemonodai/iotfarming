# Generated by Django 4.0.6 on 2022-11-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0011_alter_testcam_frame_buf'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcam',
            name='height',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='testcam',
            name='length',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='testcam',
            name='width',
            field=models.IntegerField(default=None),
        ),
    ]
