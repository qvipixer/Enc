from django.db import models
from django.shortcuts import reverse
from Enc_object.models import EncObject, EncElectricalRoom, EncProject, EncMechanism


# Create your models here.


class ElcLog(models.Model):
    record_text_title = models.CharField(
        verbose_name="Заголовок записи", max_length=100
    )

    record_text_full = models.TextField(verbose_name="Текст записи", max_length=9999)
    record_author = models.CharField(verbose_name="Автор записи", max_length=100)

    record_data_create = models.DateTimeField(
        verbose_name="Дата создания записи", auto_now=True
    )

    record_object = models.ForeignKey(
        EncObject,
        related_name="elc_log_object",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Объект",
    )

    record_electrical_room = models.ForeignKey(
        EncElectricalRoom,
        related_name="elc_log_electrical_room",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Электропомещение",
    )

    record_mechanism = models.ForeignKey(
        EncMechanism,
        related_name="elc_log_mechanism",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Механизм",
    )

    # Красивая хлебная крошка
    def __str__(self):
        return (
            f"[{self.record_author}] [{self.record_object}] [{self.record_data_create}]"
        )

    class Meta:
        verbose_name = "Запись Элекриков"
        verbose_name_plural = "Записи Элекриков"
