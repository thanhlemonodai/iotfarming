# Generated by Django 4.0.4 on 2023-01-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0021_alter_testcam_height_alter_testcam_lenght_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='fan1',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='fan2',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='pomp1',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='pomp2',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='saveEnergy',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='servor1',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='servor2',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='controlbuttoninfarm',
            name='test_fields',
            field=models.BooleanField(null=True),
        ),
    ]
