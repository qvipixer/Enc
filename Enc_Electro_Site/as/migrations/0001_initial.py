# Generated by Django 5.0.2 on 2024-02-21 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Enc_object', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_text_title', models.CharField(max_length=100, verbose_name='Заголовок записи')),
                ('record_text_full', models.TextField(max_length=9999, verbose_name='Текст записи')),
                ('record_author', models.CharField(max_length=100, verbose_name='Автор записи')),
                ('record_change_location_plc', models.BooleanField(default=False, verbose_name='Изменение в PLC')),
                ('record_change_location_hmi', models.BooleanField(default=False, verbose_name='Изменение в HMI')),
                ('record_data_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания записи')),
                ('record_electrical_room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='as_log_electrical_room', to='Enc_object.encelectricalroom', verbose_name='Электропомещение')),
                ('record_mechanism', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='as_log_mechanism', to='Enc_object.encmechanism', verbose_name='Механизм')),
                ('record_object', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='as_log_object', to='Enc_object.encobject', verbose_name='Объект')),
                ('record_project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='as_log_project', to='Enc_object.encproject', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Запись Simatic',
                'verbose_name_plural': 'Записи Simatic',
            },
        ),
    ]
