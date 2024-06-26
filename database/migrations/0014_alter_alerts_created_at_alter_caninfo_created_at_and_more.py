# Generated by Django 5.0.4 on 2024-05-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_dinputs_created_at_alter_alerts_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='devicelocation',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='devicestatus',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dinputs',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todaysdrive',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
