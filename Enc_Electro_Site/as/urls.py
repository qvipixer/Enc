from django.urls import path

from . import views
from .views import as_log_add
from .views import as_log_view

urlpatterns = [
    path("automation_log_view", as_log_view),
    path("automation_log_add", as_log_add),
    path("<int:pk>", views.ASLogViewDetails.as_view(), name="log_view-details"),
    # path("Automation_Log_View_Details", Automation_Log_View_Details),
]
