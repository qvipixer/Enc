from django.urls import path

from .views import download
from .views import page
from .views import upload
from . import views

urlpatterns = [
    path("", page),
    path("upload", upload),
    path("download", download),
]
