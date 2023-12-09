from django.shortcuts import render

from .models import Myfiles


# Create your views here.
def page(request):
    """
    all_files = Myfiles.objects.all()
    context = {
        'all_files': all_files
    }

    if request.POST:
        # print(request.POST.get('text'))
        # print(request.FILES.get('file'))
        Myfiles.objects.create(
            text=request.POST.get('text'),
            file=request.FILES.get('file')
        )
    """
    return render(request, 'index.html')


def download(request):
    all_files = Myfiles.objects.all()
    context = {
        'all_files': all_files
    }

    return render(request, 'download.html', context)
    pass


def upload(request):
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(request.GET)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(request.META.get('REMOTE_ADDR'))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
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
        print(request.META.get('REMOTE_ADDR'))
        print(request.GET)
        print(request.POST)
        print(request.FILES)
        print("!!! __GET__ !!!")

    if request.POST:
        print("!!! __POST__ !!!")
        # print(request)
        # print(request.__dict__)
        print(request.META.get('REMOTE_ADDR'))
        print(request.POST)
        print(request.FILES)
        # print(request.POST.get('text'))
        # print(request.POST.get('text_to'))
        # print(request.FILES.get('file'))
        print("!!! __POST__ !!!")

        Myfiles.objects.create(
            text=request.POST.get('text'),
            text_to=request.POST.get('text_to'),
            file=request.FILES.get('file'),
            remote_ip=request.META.get('REMOTE_ADDR')
        )

    return render(request, 'upload.html')
