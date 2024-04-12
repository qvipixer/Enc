from django.db import models
from django.shortcuts import reverse


# Create your models here.


class EncObject(models.Model):
    title = models.CharField(verbose_name="Объект", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание объекта", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="EncObject_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"
        # return f'# {self.id} {self.name}'

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class EncElectricalRoom(models.Model):
    title = models.CharField(verbose_name="Электропомещение", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание Электропомещения", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="EncElectricalRoom_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Электропомещение"
        verbose_name_plural = "Электропомещения"


class EncProject(models.Model):
    title = models.CharField(verbose_name="Проект", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание проекта", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="EncProject_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class EncMechanism(models.Model):
    title = models.CharField(verbose_name="Механизм", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание механизма", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="EncMechanism_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Механизм"
        verbose_name_plural = "Механизмы"
