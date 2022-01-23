from django import template
from ..models import *


register = template.Library()


@register.inclusion_tag('layout/navbar.html')
def get_data_for_navbar():
    production = ProductionCategory.objects.all()
    services = Services.objects.all()
    return {'production': production, 'services': services, }