from django.db import models
from django.shortcuts import reverse
from Enc_object.models import EncObject, EncElectricalRoom, EncProject, EncMechanism


# Create your models here.


class ASLog(models.Model):
    record_text_title = models.CharField(
        verbose_name="Заголовок записи", max_length=100
    )

    record_text_full = models.CharField(verbose_name="Текст записи", max_length=100)

    record_change_location_plc = models.BooleanField(
        verbose_name="Изменение в PLC", max_length=100
    )

    record_change_location_hmi = models.BooleanField(
        verbose_name="Изменение в HMI", max_length=100
    )

    record_author = models.CharField(verbose_name="Автор записи", max_length=100)

    record_data_create = models.DateTimeField(
        verbose_name="Дата создания записи", auto_now=True
    )
    record_slug = models.SlugField(max_length=50, unique=True)

    record_object = models.ForeignKey(
        EncObject,
        related_name="as_log_object",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Объект",
    )

    record_electrical_room = models.ForeignKey(
        EncElectricalRoom,
        related_name="as_log_electrical_room",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Электропомещение",
    )

    record_project = models.ForeignKey(
        EncProject,
        related_name="as_log_project",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Проект",
    )

    record_mechanism = models.ForeignKey(
        EncMechanism,
        related_name="as_log_mechanism",
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
