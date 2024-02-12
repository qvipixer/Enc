from django.contrib import admin
from .models import (
    ASLog,
)


# Register your models here.


class ASLogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"record_slug": ("record_text_title",)}
    # prepopulated_fields = {"record_slug": ("id=" + "id" + " " + "record_text_title",)}


admin.site.register(ASLog, ASLogAdmin)
