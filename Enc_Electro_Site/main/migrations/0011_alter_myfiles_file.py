# Generated by Django 5.0.2 on 2024-04-11 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_alter_myfiles_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myfiles",
            name="file",
            field=models.FileField(
                upload_to="upload_file/2024-04-11/", verbose_name="Файл"
            ),
        ),
    ]
