from django.contrib import admin
from .models import (
    ASLog,
)


# Register your models here.


class ASLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(ASLog, ASLogAdmin)
