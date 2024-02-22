from django.urls import path

from . import views
from .views import as_log_add
from .views import as_log_view
from .views import SearchResultsView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="as_search_results"),
    path("as_log_view", as_log_view, name="as_log_view"),
    path("as_log_add", as_log_add, name="as_log_add"),
    path(
        "as_log_view/details/log/<int:pk>",
        views.ASLogViewDetails.as_view(),
        name="new_as_log_view_details",
    ),
]
