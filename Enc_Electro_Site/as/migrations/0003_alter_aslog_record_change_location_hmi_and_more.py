# Generated by Django 5.0.1 on 2024-02-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("as", "0002_alter_aslog_record_change_location_hmi_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aslog",
            name="record_change_location_hmi",
            field=models.BooleanField(default=False, verbose_name="Изменение в HMI"),
        ),
        migrations.AlterField(
            model_name="aslog",
            name="record_change_location_plc",
            field=models.BooleanField(default=False, verbose_name="Изменение в PLC"),
        ),
    ]
