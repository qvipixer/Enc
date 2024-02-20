from django.contrib import admin
from .models import ElcLog


# Register your models here.


class ElcASLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(ElcLog, ElcASLogAdmin)
