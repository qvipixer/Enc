# Generated by Django 5.0.2 on 2024-02-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EncElectricalRoom",
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
                    "title",
                    models.CharField(max_length=100, verbose_name="Электропомещение"),
                ),
                (
                    "title_description",
                    models.CharField(
                        max_length=100, verbose_name="Описание Электропомещения"
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Электропомещение",
                "verbose_name_plural": "Электропомещения",
            },
        ),
        migrations.CreateModel(
            name="EncMechanism",
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
                ("title", models.CharField(max_length=100, verbose_name="Механизм")),
                (
                    "title_description",
                    models.CharField(max_length=100, verbose_name="Описание механизма"),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Механизм",
                "verbose_name_plural": "Механизмы",
            },
        ),
        migrations.CreateModel(
            name="EncObject",
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
                ("title", models.CharField(max_length=100, verbose_name="Объект")),
                (
                    "title_description",
                    models.CharField(max_length=100, verbose_name="Описание объекта"),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Объект",
                "verbose_name_plural": "Объекты",
            },
        ),
        migrations.CreateModel(
            name="EncProject",
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
                ("title", models.CharField(max_length=100, verbose_name="Проект")),
                (
                    "title_description",
                    models.CharField(max_length=100, verbose_name="Описание проекта"),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Проект",
                "verbose_name_plural": "Проекты",
            },
        ),
    ]
