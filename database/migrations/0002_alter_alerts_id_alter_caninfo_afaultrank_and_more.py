# Generated by Django 5.0.4 on 2024-05-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='AFaultRank',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='AMaxCellVolt',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='AMinCellVolt',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='APackCurrentValue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='APackVoltageValue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='ASOCValue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='BFaultRank',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='BMaxCellVolt',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='BMinCellVolt',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='BPackCurrentValue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='BPackVoltageValue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='BSOCValue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='ChargerGunDetected2',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='batteryTemperature',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='distanceToEmpty',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='stateOfCharge',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='totalRegenerationEnergy',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='caninfo',
            name='vehicleBattery',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='devicelocation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dinputs',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='links',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='todaysdrive',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
