from django.shortcuts import render

from .models import ASLog, EncObject, EncProject, EncElectricalRoom, EncMechanism

from django.views.generic import DetailView

as_log_records_count = ASLog.objects.count()

# Create your views here.


# Create your views here.
def as_log_add(request):
    all_automation_categories = ASLog.objects.all()
    all_enc_object = EncObject.objects.all()
    all_enc_project = EncProject.objects.all()
    all_enc_electrical_room = EncElectricalRoom.objects.all()
    all_enc_mechanism = EncMechanism.objects.all()

    if request.POST:
        print("!!! __POST__ !!!")
        print(request.POST)
        print("!!! __POST__ !!!")

        # <QueryDict:
        # {
        # 'csrfmiddlewaretoken': ['tNEmUvq2qwIea9mz3NBIgV19bX1oZ95VMYJe18Ha10fBC1vBRZHJ3XkXT5OASt7S'],
        # 'text_to_record_text_title': [''],
        # 'record_change_location_plc': ['on'],
        # 'record_change_location_hmi': ['on'],
        # 'record_object': ['el.title'],
        # 'record_electrical_room': ['el.title'],
        # 'record_project': ['el.title'],
        # 'record_mechanism': ['el.title']
        # }
        # >

        ASLog.objects.create(
            record_author=request.POST.get("record_author"),
            record_text_title=request.POST.get("record_text_title"),
            record_text_full=request.POST.get("record_text_full"),
            record_change_location_plc=request.POST.get("record_change_location_plc"),
            record_change_location_hmi=request.POST.get("record_change_location_hmi"),
            record_object=request.POST.get("record_object"),
            record_electrical_room=request.POST.get("record_electrical_room"),
            record_project=request.POST.get("record_project"),
            record_mechanism=request.POST.get("record_mechanism"),
            record_data_create=request.POST.get("record_data_create"),
        )

    return render(
        request,
        template_name="as/log/log_add.html",
        context={
            "title": "Добавление в журнал",
            "all_automation_categories": all_automation_categories,
            "all_enc_object": all_enc_object,
            "all_enc_project": all_enc_project,
            "all_enc_electrical_room": all_enc_electrical_room,
            "all_enc_mechanism": all_enc_mechanism,
            "as_log_records_count": as_log_records_count,
        },
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
            "as_log_records_count": as_log_records_count,
        },
    )


class ASLogViewDetails(DetailView):
    model = ASLog
    # template_file = "as/log/log_view_details.html"
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
