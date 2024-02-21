from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from .models import Myfiles


def page(request):
    print(request.user)
    # files_count = Myfiles.objects.count()
    # print(files_count)
    return render(
        request,
        template_name="main/index.html",
        context={
            "title": "Главная страница",
            "aut_user": request.user,
        },
    )


def file_download(request):
    all_files = Myfiles.objects.order_by("-id")[:10]

    return render(
        request,
        template_name="main/file/download.html",
        context={
            "all_files": all_files,
            "title": "Скачать файлы",
        },
    )


def file_upload(request):
    # print(
    #     "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    # )
    # print(request.META.get("REMOTE_ADDR"))
    # print(
    #     "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    # )
    # if request.GET:
    # print("!!! __GET__ !!!")
    # print(request.META.get("REMOTE_ADDR"))
    # print(request.GET)
    # print(request.POST)
    # print(request.FILES)
    # print("!!! __GET__ !!!")

    if request.POST:
        # print("!!! __POST__ !!!")
        # print(request.META.get("REMOTE_ADDR"))
        # print(request.POST)
        # print(request.FILES)
        # print("!!! __POST__ !!!")

        Myfiles.objects.create(
            text=request.user,
            text_to=request.POST.get("text_to"),
            file=request.FILES.get("file"),
            remote_ip=request.META.get("REMOTE_ADDR"),
        )

    # return render(request, 'upload.html')
    return render(
        request,
        template_name="main/file/upload.html",
        context={
            "title": "Загрузка файлов",
            "aut_user": request.user,
        },
    )


def user_login(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(username)
        # print(password)
        # print(user)

        if user is not None:
            login(request, user=user)
            return redirect("main_page")

    return render(request, template_name="main/auth/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
