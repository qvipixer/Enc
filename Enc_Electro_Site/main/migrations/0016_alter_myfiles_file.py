# Generated by Django 5.0.2 on 2024-05-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_alter_myfiles_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myfiles",
            name="file",
            field=models.FileField(
                upload_to="upload_file/2024-05-21/", verbose_name="Файл"
            ),
        ),
    ]
