from django.contrib import admin
from .models import (
    ASLog,
    ASLogObject,
    ASLogProjectSub,
    ASLogProject,
    ASLogObjectSub,
)


# Register your models here.


class ASLogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"record_slug": ("record_text_title",)}
    # prepopulated_fields = {"record_slug": ("id=" + "id" + " " + "record_text_title",)}
    pass


admin.site.register(ASLog, ASLogAdmin)


class ASLogObjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass


admin.site.register(ASLogObject, ASLogObjectAdmin)


class ASLogObjectSubAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass


admin.site.register(ASLogObjectSub, ASLogObjectSubAdmin)


class ASLogProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass


admin.site.register(ASLogProject, ASLogProjectAdmin)


class ASLogProjectSubAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass


admin.site.register(ASLogProjectSub, ASLogProjectSubAdmin)
