from django.contrib import admin
from .models import (
    ASLog,
)


# Register your models here.


class ASLogAdmin(admin.ModelAdmin):
    list_display = ("record_text_title", "record_object", "record_data_create")
    list_filter = (
        "record_change_location_plc",
        "record_change_location_hmi",
        "record_object",
        "record_electrical_room",
        "record_project",
        "record_mechanism",
    )


admin.site.register(ASLog, ASLogAdmin)
