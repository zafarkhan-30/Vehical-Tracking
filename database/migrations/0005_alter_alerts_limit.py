# Generated by Django 5.0.4 on 2024-05-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_alerts_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='limit',
            field=models.IntegerField(null=True),
        ),
    ]
