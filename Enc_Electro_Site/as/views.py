from django.shortcuts import render
from django.db.models import Q  # новый
from .models import ASLog, EncObject, EncProject, EncElectricalRoom, EncMechanism

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
            "title": "Добавление в журнал Группы Автоматики",
            "all_automation_categories": all_automation_categories,
            "all_enc_object": all_enc_object,
            "all_enc_project": all_enc_project,
            "all_enc_electrical_room": all_enc_electrical_room,
            "all_enc_mechanism": all_enc_mechanism,
        },
    )


def as_log_view(request):
    # all_automation_log = ASLog.objects.order_by("-id")[:10]
    all_automation_log = ASLog.objects.all().order_by("-id")

    p = Paginator(all_automation_log, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get("page")
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {"page_obj": page_obj}

    # sending the page object to index.html
    page_values = page_obj.object_list.values()

    return render(
        request,
        template_name="as/log/log_view.html",
        context={
            "title": "Просмотр журнала Группы Автоматики",
            "page_obj": page_obj,
            "context": context,
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
