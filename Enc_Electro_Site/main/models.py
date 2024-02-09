from django.db import models
from django.shortcuts import reverse


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
