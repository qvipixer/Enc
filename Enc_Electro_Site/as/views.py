from django.shortcuts import render
from .models import ASLog
from django.views.generic import DetailView

# Create your views here.


# Create your views here.
def as_log_add(request):
    return render(
        request,
        template_name="as/log/log_add.html",
        context={"title": "Добавление в журнал"},
    )


def as_log_view(request):
    all_automation_log = ASLog.objects.order_by("-id")[:10]
    # all_automation_log = ASLog.objects.all()
    # print(all_automation_log)
    return render(
        request,
        template_name="as/log/log_view.html",
        context={
            "title": "Просмотр журнала",
            "all_automation_log": all_automation_log,
        },
    )


class ASLogViewDetails(DetailView):
    model = ASLog
    template_file = "as/log/log_view_details.html"
    context_object_name = "log_view_details"


# def Automation_Log_View_Details(request):
#     all_AutomationLog_Details = AutomationLog.objects.all()
#     all_AutomationLog = request.GET.get("Automation_Log_View")  # GET переменная
#     print()
#     print("all_AutomationLog_Details")
#     print(all_AutomationLog_Details)
#     print()
#     print("all_AutomationLog")
#     print(all_AutomationLog)
#     return render(
#         request,
#         template_name="main/Automation_Log_View_Details.html",
#         context={
#             "title": "Подробно об ",
#             "all_AutomationLog": all_AutomationLog,
#             "all_AutomationLog_Details": all_AutomationLog_Details,
#         },
#     )
