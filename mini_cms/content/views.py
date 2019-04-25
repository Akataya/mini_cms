from django.shortcuts import render
from .models import Announcement, Section, SectionItem, Office
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    announcement_list = Announcement.objects.all()
    data = {
        'announcement_list': announcement_list,
    }
    return render(request, 'content/index.html', context=data)


@login_required
def section(request, pk):
    section = Section.objects.get(id=pk)
    items = SectionItem.objects.filter(section=section)
    data = {
        'section': section,
        'items': items
    }
    return render(request, 'content/section.html', context=data)


class OfficeListView(LoginRequiredMixin, ListView):
    model = Office
