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


class AutomationLog_Object_Sub(models.Model):
    title = models.CharField(verbose_name="Электропомещение", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание Электропомещения", max_length=100
    )


class AutomationLog_Pproject(models.Model):
    title = models.CharField(verbose_name="Проект", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание проекта", max_length=100
    )


class AutomationLog_Pproject_Sub(models.Model):
    title = models.CharField(verbose_name="Механизм", max_length=100)
    title_description = models.CharField(
        verbose_name="Описание механизма", max_length=100
    )


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
        verbose_name="Категория",
    )

    record_object_sub = models.ForeignKey(
        AutomationLog_Object_Sub,
        related_name="record_object_sub",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Подкатегория",
    )

    record_project = models.ForeignKey(
        AutomationLog_Pproject,
        related_name="record_project",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Подкатегория",
    )

    record_project_sub = models.ForeignKey(
        AutomationLog_Pproject_Sub,
        related_name="record_project_sub",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Подкатегория",
    )

    # def __str__(self):
    #    return f"# {self.id} {self.text} от: [{self.text_to}] кому: [{self.file}]"
    #    # return f'# {self.id} {self.name}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
