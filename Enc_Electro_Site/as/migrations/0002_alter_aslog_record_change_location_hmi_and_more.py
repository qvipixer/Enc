# Generated by Django 5.0.1 on 2024-02-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("as", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aslog",
            name="record_change_location_hmi",
            field=models.CharField(max_length=100, verbose_name="Изменение в HMI"),
        ),
        migrations.AlterField(
            model_name="aslog",
            name="record_change_location_plc",
            field=models.CharField(max_length=100, verbose_name="Изменение в PLC"),
        ),
        migrations.AlterField(
            model_name="aslog",
            name="record_text_full",
            field=models.CharField(max_length=9999, verbose_name="Текст записи"),
        ),
    ]