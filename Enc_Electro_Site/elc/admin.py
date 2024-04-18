from django.contrib import admin
from .models import ElcLog


# Register your models here.


class ElcASLogAdmin(admin.ModelAdmin):
    list_display = ("record_text_title", "record_object", "record_data_create")
    list_filter = (
        "record_object",
        "record_electrical_room",
        "record_mechanism",
    )


admin.site.register(ElcLog, ElcASLogAdmin)
