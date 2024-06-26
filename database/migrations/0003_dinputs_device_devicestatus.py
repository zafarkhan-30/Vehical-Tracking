# Generated by Django 5.0.4 on 2024-05-05 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_alerts_id_alter_caninfo_afaultrank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinputs',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_dinputs', to='database.devices'),
        ),
        migrations.CreateModel(
            name='deviceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deviceStatus', to='database.devices')),
            ],
        ),
    ]
