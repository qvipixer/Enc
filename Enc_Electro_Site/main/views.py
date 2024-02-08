from django.shortcuts import render

from .models import Myfiles
from .models import AutomationLog


# Create your views here.
def automation_log_view(request):
    all_automation_log = AutomationLog.objects.all()
    print(all_automation_log)
    return render(
        request,
        template_name="main/Automation_Log_View.html",
        context={
            "title": "Просмотр журнала",
            "all_automation_log": all_automation_log,
        },
    )


def Automation_Log_View_Details(request):
    all_AutomationLog_Details = AutomationLog.objects.all()
    all_AutomationLog = request.GET.get("Automation_Log_View")  # GET переменная
    print()
    print("all_AutomationLog_Details")
    print(all_AutomationLog_Details)
    print()
    print("all_AutomationLog")
    print(all_AutomationLog)
    return render(
        request,
        template_name="main/Automation_Log_View_Details.html",
        context={
            "title": "Подробно об ",
            "all_AutomationLog": all_AutomationLog,
            "all_AutomationLog_Details": all_AutomationLog_Details,
        },
    )


def Automation_Log_Add(request):
    return render(
        request,
        template_name="main/Automation_Log_Add.html",
        context={"title": "Добавление в журнал"},
    )


def page(request):
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
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(request.META.get("REMOTE_ADDR"))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
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
