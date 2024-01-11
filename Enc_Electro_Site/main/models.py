from django.db import models


# Create your models here.
class Myfiles(models.Model):
    text = models.CharField(verbose_name="Отправитель файла", max_length=100)
    text_to = models.CharField(verbose_name="Получатель файла", max_length=100)
    remote_ip = models.GenericIPAddressField(
        verbose_name="IP адрес отправителя файла",
    )
    file = models.FileField(verbose_name="Файл", upload_to="upload_file/")
    data_create = models.DateTimeField(
        verbose_name="Дата загрузки файла", auto_now=True
    )

    def __str__(self):
        return f"# {self.id} {self.text} от: [{self.text_to}] кому: [{self.file}]"
        # return f'# {self.id} {self.name}'

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class AutomationLog_Object(models.Model):
    title = models.CharField(verbose_name="Объекта", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание объекта", max_length=100
    )

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"
        # return f'# {self.id} {self.name}'

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class AutomationLog_Object_Sub(models.Model):
    title = models.CharField(verbose_name="Электропомещение", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание Электропомещения", max_length=100
    )

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Электропомещение"
        verbose_name_plural = "Электропомещения"


class AutomationLog_Project(models.Model):
    title = models.CharField(verbose_name="Проект", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание проекта", max_length=100
    )

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class AutomationLog_Project_Sub(models.Model):
    title = models.CharField(verbose_name="Механизм", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание механизма", max_length=100
    )

    # Красивая хлебная крошка
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Механизм"
        verbose_name_plural = "Механизмы"


class MyAutomationLog(models.Model):
    record_text = models.CharField(verbose_name="Текст записи", max_length=100)
    record_text_description = models.CharField(
        verbose_name="Короткий текст записи", max_length=100
    )
    record_author = models.CharField(verbose_name="Автор", max_length=100)
    # file = models.FileField(verbose_name="Файл", upload_to='upload_file/')
    record_data_create = models.DateTimeField(
        verbose_name="Дата создания записи", auto_now=True
    )

    record_object = models.ForeignKey(
        AutomationLog_Object,
        related_name="record_object",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Объект",
    )

    record_object_sub = models.ForeignKey(
        AutomationLog_Object_Sub,
        related_name="record_object_sub",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Электропомещение",
    )

    record_project = models.ForeignKey(
        AutomationLog_Project,
        related_name="record_project",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Проект",
    )

    record_project_sub = models.ForeignKey(
        AutomationLog_Project_Sub,
        related_name="record_project_sub",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Механизм",
    )

    # Красивая хлебная крошка
    def __str__(self):
        return (
            f"[{self.record_author}] [{self.record_object}] [{self.record_data_create}]"
        )
        # return f'# {self.id} {self.name}'

    # def __str__(self):
    #    return "{}".format(self.id)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
