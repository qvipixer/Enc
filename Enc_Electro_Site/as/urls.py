from django.urls import path

from . import views
from .views import as_log_add
from .views import as_log_view

urlpatterns = [
    path("as_log_view", as_log_view, name="as_log_view"),
    path("as_log_add", as_log_add, name="as_log_add"),
    path(
        "as_log_view/details/log/<int:pk>",
        views.ASLogViewDetails.as_view(),
        name="new_log_view_details",
    ),
]
