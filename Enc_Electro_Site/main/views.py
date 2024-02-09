from django.shortcuts import render, redirect

from .models import Myfiles
from django.contrib.auth import login, logout, authenticate


def page(request):
    print(request.user)
    return render(
        request,
        template_name="main/index.html",
        context={"title": "Главная страница", "aut_user": request.user},
    )


def download(request):
    # """
    # all_files = Myfiles.objects.all()
    # context = {
    #     'all_files': all_files
    # }
    #
    # return render(request, 'download.html', context)
    # """

    all_files = Myfiles.objects.all()
    return render(
        request,
        template_name="main/file/download.html",
        context={"all_files": all_files},
    )


def upload(request):
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
            text=request.POST.get("text"),
            text_to=request.POST.get("text_to"),
            file=request.FILES.get("file"),
            remote_ip=request.META.get("REMOTE_ADDR"),
        )

    # return render(request, 'upload.html')
    return render(
        request,
        template_name="main/file/upload.html",
        context={"title": "Загрузка файлов", "aut_user": request.user},
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
