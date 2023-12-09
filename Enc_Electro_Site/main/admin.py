from django.contrib import admin

from .models import Myfiles


# Register your models here.
class Myfiles_Admin(admin.ModelAdmin):
    pass


admin.site.register(Myfiles, Myfiles_Admin)
