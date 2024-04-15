# https://tutorial.djangogirls.org/ru/django_forms/


from django.shortcuts import render

from .models import ElcLog, EncObject, EncProject, EncElectricalRoom, EncMechanism
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, ListView

from .forms import ElcLogAddForm
from django.shortcuts import redirect
from django.utils import timezone


# Create your views here.
def elc_log_add(request):
    all_electrical_categories = ElcLog.objects.all()
    all_enc_object = EncObject.objects.all()
    all_enc_project = EncProject.objects.all()
    all_enc_electrical_room = EncElectricalRoom.objects.all()
    all_enc_mechanism = EncMechanism.objects.all()

    elc_log_add_form = ElcLogAddForm(request.POST)

    if request.POST:
        elc_log_add_form = ElcLogAddForm(request.POST)
        if elc_log_add_form.is_valid():
            post = elc_log_add_form.save(commit=False)
            post.record_author = request.user
            post.record_data_create = timezone.now()
            post.save()
            return redirect(to="new_elc_log_view_details", pk=post.pk)
    else:
        elc_log_add_form = ElcLogAddForm()
    return render(
        request,
        template_name="elc/log/log_add.html",
        context={
            "elc_log_add_form": elc_log_add_form,
            "title": "Добавление в журнал Электриков",
            "all_electrical_categories": all_electrical_categories,
            "all_enc_object": all_enc_object,
            "all_enc_project": all_enc_project,
            "all_enc_electrical_room": all_enc_electrical_room,
            "all_enc_mechanism": all_enc_mechanism,
        },
    )


def elc_log_view(request):
    all_electrical_log = ElcLog.objects.order_by("-id")[:10]

    posts = ElcLog.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
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

    return render(
        request,
        template_name="elc/log/log_view.html",
        context={
            "title": "Просмотр журнала Электриков",
            "all_electrical_log": all_electrical_log,
            "page_obj": page_obj,
            "context": context,
        },
    )


def elc_log_view_listing(request):
    posts = ElcLog.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
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
    return render(request, "elc/log/elc_log_view_listing.html", context)


class ElcLogLogViewDetails(DetailView):
    model = ElcLog
    context_object_name = "log_view_details"


# class ElcLogLogListView(ListView):
#     paginate_by = 2
#     model = ElcLog
