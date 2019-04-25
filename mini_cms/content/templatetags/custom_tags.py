from django import template
from ..models import Section, Office

register = template.Library()


@register.simple_tag
def get_menu():
    section_list = Section.objects.all()
    return section_list


@register.simple_tag
def get_office_list_not_empty():
    offices = Office.objects.all()
    if offices:
        return True
    else:
        return False
