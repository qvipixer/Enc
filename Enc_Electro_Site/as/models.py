from django.db import models
from django.shortcuts import reverse

# Create your models here.


class ASLogObject(models.Model):
    title = models.CharField(verbose_name="Объект", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание объекта", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="ASLog_Object_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"
        # return f'# {self.id} {self.name}'

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class ASLogObjectSub(models.Model):
    title = models.CharField(verbose_name="Электропомещение", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание Электропомещения", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="ASLog_Object_Sub_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Электропомещение"
        verbose_name_plural = "Электропомещения"


class ASLogProject(models.Model):
    title = models.CharField(verbose_name="Проект", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание проекта", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="ASLog_Project_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ASLogProjectSub(models.Model):
    title = models.CharField(verbose_name="Механизм", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание механизма", max_length=100
    )
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse(viewname="ASLog_Project_Sub_url", kwargs={"slug": self.slug})

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Механизм"
        verbose_name_plural = "Механизмы"


class ASLog(models.Model):
    record_text_title = models.CharField(
        verbose_name="Заголовок записи", max_length=100
    )

    record_text_description = models.CharField(
        verbose_name="Короткий текст записи", max_length=100
    )

    record_text_full = models.CharField(verbose_name="Текст записи", max_length=100)
    record_text_full_plc = models.CharField(
        verbose_name="Текст записи PLC", max_length=100
    )
    record_text_full_hmi = models.CharField(
        verbose_name="Текст записи HMI", max_length=100
    )
    record_text_full_hmi_to_plc = models.CharField(
        verbose_name="Текст записи из HMI в PLC", max_length=100
    )
    record_text_full_plc_to_hmi = models.CharField(
        verbose_name="Текст записи из PLC в HMI", max_length=100
    )
    record_author = models.CharField(verbose_name="Автор записи", max_length=100)
    # file = models.FileField(verbose_name="Файл", upload_to='upload_file/')
    record_data_create = models.DateTimeField(
        verbose_name="Дата создания записи", auto_now=True
    )
    record_slug = models.SlugField(max_length=50, unique=True)

    record_object = models.ForeignKey(
        ASLogObject,
        related_name="record_object",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Объект",
    )

    record_object_sub = models.ForeignKey(
        ASLogObjectSub,
        related_name="record_object_sub",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Электропомещение",
    )

    record_project = models.ForeignKey(
        ASLogProject,
        related_name="record_project",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Проект",
    )

    record_project_sub = models.ForeignKey(
        ASLogProjectSub,
        related_name="record_project_sub",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Механизм",
    )
    """
    def get_absolute_url(self):
        return reverse(
            viewname="AS_record_url", kwargs={"record_slug": self.record_slug}
        )
    """

    def get_absolute_url(self):
        return self.record_slug

    # Красивая хлебная крошка
    def __str__(self):
        return (
            f"[{self.record_author}] [{self.record_object}] [{self.record_data_create}]"
        )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
