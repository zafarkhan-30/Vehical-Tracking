# Generated by Django 5.0.4 on 2024-05-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_dinputs_device_devicestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='address',
            field=models.CharField(max_length=1000),
        ),
    ]