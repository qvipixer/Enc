# Generated by Django 5.0.1 on 2024-02-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myfiles",
            name="file",
            field=models.FileField(
                upload_to="upload_file/2024-02-22/", verbose_name="Файл"
            ),
        ),
    ]