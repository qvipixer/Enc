from django.contrib import admin

from .models import (
    Myfiles,
    MyAutomationLog,
    AutomationLog_Object,
    AutomationLog_Object_Sub,
    AutomationLog_Project,
    AutomationLog_Project_Sub,
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


class AutomationLog_Project_Admin(admin.ModelAdmin):
    pass


admin.site.register(AutomationLog_Project, AutomationLog_Project_Admin)


class AutomationLog_Project_Sub_Admin(admin.ModelAdmin):
    pass


admin.site.register(AutomationLog_Project_Sub, AutomationLog_Project_Sub_Admin)
