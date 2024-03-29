# Generated by Django 5.0.2 on 2024-02-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Myfiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.CharField(max_length=100, verbose_name="Отправитель файла"),
                ),
                (
                    "text_to",
                    models.CharField(max_length=100, verbose_name="Получатель файла"),
                ),
                (
                    "remote_ip",
                    models.GenericIPAddressField(
                        verbose_name="IP адрес отправителя файла"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="upload_file/2024-02-21/", verbose_name="Файл"
                    ),
                ),
                (
                    "data_create",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата загрузки файла"
                    ),
                ),
            ],
            options={
                "verbose_name": "Файл",
                "verbose_name_plural": "Файлы",
            },
        ),
    ]
