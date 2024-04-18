from django.urls import path

from . import views
from .views import elc_log_add
from .views import elc_log_view

# from .views import elc_log_view_listing

urlpatterns = [
    path("elc_log_view", elc_log_view, name="elc_log_view"),
    # path("elc_log_view_listing", elc_log_view_listing, name="elc_log_view_listing"),
    path("elc_log_add", elc_log_add, name="elc_log_add"),
    path(
        "elc_log_view/details/log/<int:pk>",
        views.ElcLogLogViewDetails.as_view(),
        name="new_elc_log_view_details",
    ),
]
