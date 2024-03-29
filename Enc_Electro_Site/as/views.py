from django.shortcuts import render
from django.db.models import Q  # новый
from .models import ASLog, EncObject, EncProject, EncElectricalRoom, EncMechanism

from django.views.generic import DetailView, ListView, TemplateView

from .forms import AsLogAddForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.


def as_log_add(request):
    all_automation_categories = ASLog.objects.all()
    all_enc_object = EncObject.objects.all()
    all_enc_project = EncProject.objects.all()
    all_enc_electrical_room = EncElectricalRoom.objects.all()
    all_enc_mechanism = EncMechanism.objects.all()

    as_log_add_form = AsLogAddForm(request.POST)

    if request.POST:
        as_log_add_form = AsLogAddForm(request.POST)
        if as_log_add_form.is_valid():
            post = as_log_add_form.save(commit=False)
            post.record_author = request.user
            post.record_data_create = timezone.now()
            post.save()
            return redirect(to="new_as_log_view_details", pk=post.pk)
    else:
        as_log_add_form = AsLogAddForm()
    return render(
        request,
        template_name="as/log/log_add.html",
        context={
            "as_log_add_form": as_log_add_form,
            "title": "Добавление в журнал",
            "all_automation_categories": all_automation_categories,
            "all_enc_object": all_enc_object,
            "all_enc_project": all_enc_project,
            "all_enc_electrical_room": all_enc_electrical_room,
            "all_enc_mechanism": all_enc_mechanism,
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
        },
    )


class ASLogViewDetails(DetailView):
    model = ASLog
    # template_file = "as/log/log_view_details.html"
    context_object_name = "log_view_details"


class SearchResultsView(ListView):
    model = ASLog
    template_name = "search_results.html"

    def get_queryset(self):  # новый
        query = self.request.GET.get("search")
        object_list = ASLog.objects.filter(
            Q(record_text_full__icontains=query)
            # or Q(record_text_title__icontains=query)
            # or Q(record_object__icontains=query)
            # or Q(record_electrical_room__icontains=query)
        )
        return object_list
