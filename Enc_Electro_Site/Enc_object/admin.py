from django.contrib import admin
from .models import EncObject, EncProject, EncElectricalRoom, EncMechanism

# Register your models here.


class EncObjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(EncObject, EncObjectAdmin)


class EncProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(EncProject, EncProjectAdmin)


class EncElectricalRoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(EncElectricalRoom, EncElectricalRoomAdmin)


class EncMechanismAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title_description",)}


admin.site.register(EncMechanism, EncMechanismAdmin)
