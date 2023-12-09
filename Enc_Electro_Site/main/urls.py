from django.urls import path

from .views import download
from .views import page
from .views import upload

urlpatterns = [
    path('', page),
    path('upload', upload),
    path('download', download)

]
