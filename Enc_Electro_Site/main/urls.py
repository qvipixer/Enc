from django.urls import path

from .views import file_download
from .views import page
from .views import file_upload
from .views import user_login
from .views import user_logout

urlpatterns = [
    path("", page, name="main_page"),
    path("upload", file_upload, name="upload"),
    path("download", file_download, name="download"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
