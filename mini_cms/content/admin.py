from django.contrib import admin
from .models import Announcement, Section, SectionItem, Office
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.site_header = 'Administration'


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    list_display = ['id', 'title', 'posted']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = ['id', 'title']


@admin.register(SectionItem)
class PolicyItemAdmin(admin.ModelAdmin):
    model = SectionItem
    list_display = ['id', 'title', 'section']


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    model = Office
    list_display = ['number', 'name', 'abbreviation']
