# Generated by Django 4.0.6 on 2022-11-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0009_controlbuttoninfarm_test_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_buf', models.BinaryField(default=b'abc')),
            ],
        ),
    ]