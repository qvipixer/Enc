from django.shortcuts import render

from .models import Myfiles


# Create your views here.
def page(request):
    # return render(request, 'index.html')
    return render(
        request,
        template_name="main/index.html",
        context={"title": "Главная страница"},
    )


def download(request):
    """
    all_files = Myfiles.objects.all()
    context = {
        'all_files': all_files
    }

    return render(request, 'download.html', context)
    """

    all_files = Myfiles.objects.all()
    return render(
        request,
        template_name="main/download.html",
        context={"all_files": all_files},
    )


def upload(request):
    print(
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )
    print(request.META.get("REMOTE_ADDR"))
    print(
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )
    if request.GET:
        print("!!! __GET__ !!!")
        print(request.META.get("REMOTE_ADDR"))
        print(request.GET)
        print(request.POST)
        print(request.FILES)
        print("!!! __GET__ !!!")

    if request.POST:
        print("!!! __POST__ !!!")
        print(request.META.get("REMOTE_ADDR"))
        print(request.POST)
        print(request.FILES)
        print("!!! __POST__ !!!")

        Myfiles.objects.create(
            text=request.POST.get("text"),
            text_to=request.POST.get("text_to"),
            file=request.FILES.get("file"),
            remote_ip=request.META.get("REMOTE_ADDR"),
        )

    # return render(request, 'upload.html')
    return render(
        request,
        template_name="main/upload.html",
        context={"title": "Загрузка файлов"},
    )
