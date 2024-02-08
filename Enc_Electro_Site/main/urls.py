from django.urls import path

from .views import download
from .views import page
from .views import upload
from .views import automation_log_view
from .views import Automation_Log_View_Details
from .views import Automation_Log_Add


urlpatterns = [
    path("", page),
    path("upload", upload),
    path("download", download),
    path("Automation_Log_View", automation_log_view),
    path("Automation_Log_View_Details", Automation_Log_View_Details),
    path("Automation_Log_Add", Automation_Log_Add),
]
