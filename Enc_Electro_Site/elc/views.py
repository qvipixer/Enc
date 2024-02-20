# https://tutorial.djangogirls.org/ru/django_forms/


from django.shortcuts import render

from .models import ElcLog, EncObject, EncProject, EncElectricalRoom, EncMechanism

from django.views.generic import DetailView

from .forms import ElcLogAddForm
from django.shortcuts import redirect
from django.utils import timezone

elc_log_records_count = ElcLog.objects.count()

# Create your views here.


# Create your views here.
def elc_log_add(request):
    all_electrical_categories = ElcLog.objects.all()
    all_enc_object = EncObject.objects.all()
    all_enc_project = EncProject.objects.all()
    all_enc_electrical_room = EncElectricalRoom.objects.all()
    all_enc_mechanism = EncMechanism.objects.all()

    elc_log_add_form = ElcLogAddForm(request.POST)

    if request.method == "POST":
        elc_log_add_form = ElcLogAddForm(request.POST)
        if elc_log_add_form.is_valid():
            post = elc_log_add_form.save(commit=False)
            post.record_author = request.user
            post.record_data_create = timezone.now()
            post.save()
            return redirect("new_log_view_details", pk=post.pk)
    else:
        as_log_add_form = ElcLogAddForm()
    return render(
        request,
        "elc/log/log_add.html",
        {
            "elc_log_add_form": elc_log_add_form,
            "title": "Добавление в журнал",
        },
    )


def elc_log_view(request):
    all_electrical_log = ElcLog.objects.order_by("-id")[:10]

    return render(
        request,
        template_name="elc/log/log_view.html",
        context={
            "title": "Просмотр журнала",
            "all_electrical_log": all_electrical_log,
            "elc_log_records_count": elc_log_records_count,
        },
    )


class ElcLogLogViewDetails(DetailView):
    model = ElcLog
    context_object_name = "log_view_details"
