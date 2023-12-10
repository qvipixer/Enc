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
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(request.GET)
    print(
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )
    print(request.META.get("REMOTE_ADDR"))
    print(
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )
    # print(request.POST)
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(request.FILES)
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # print(request.__dict__)
    # print(request.POST.get('text'))
    # print(request.POST.get('text_to'))
    # print(request.FILES.get('file'))
    if request.GET:
        print("!!! __GET__ !!!")
        print(request.META.get("REMOTE_ADDR"))
        print(request.GET)
        print(request.POST)
        print(request.FILES)
        print("!!! __GET__ !!!")

    if request.POST:
        print("!!! __POST__ !!!")
        # print(request)
        # print(request.__dict__)
        print(request.META.get("REMOTE_ADDR"))
        print(request.POST)
        print(request.FILES)
        # print(request.POST.get('text'))
        # print(request.POST.get('text_to'))
        # print(request.FILES.get('file'))
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
