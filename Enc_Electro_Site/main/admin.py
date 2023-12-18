from django.contrib import admin

from .models import (
    Myfiles,
    MyAutomationLog,
    AutomationLog_Object,
    AutomationLog_Object_Sub,
    AutomationLog_Pproject,
    AutomationLog_Pproject_Sub,
)


# Register your models here.
class Myfiles_Admin(admin.ModelAdmin):
    pass


admin.site.register(Myfiles, Myfiles_Admin)


class MyAutomationLog_Admin(admin.ModelAdmin):
    pass


admin.site.register(MyAutomationLog, MyAutomationLog_Admin)


class AutomationLog_Object_Admin(admin.ModelAdmin):
    pass


admin.site.register(AutomationLog_Object, AutomationLog_Object_Admin)


class AutomationLog_Object_Sub_Admin(admin.ModelAdmin):
    pass


admin.site.register(AutomationLog_Object_Sub, AutomationLog_Object_Sub_Admin)


class AutomationLog_Pproject_Admin(admin.ModelAdmin):
    pass


admin.site.register(AutomationLog_Pproject, AutomationLog_Pproject_Admin)


class AutomationLog_Pproject_Sub_Admin(admin.ModelAdmin):
    pass


admin.site.register(AutomationLog_Pproject_Sub, AutomationLog_Pproject_Sub_Admin)
