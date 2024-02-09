from django.contrib import admin

from .models import (
    Myfiles,
)


# Register your models here.
class MyfilesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Myfiles, MyfilesAdmin)
