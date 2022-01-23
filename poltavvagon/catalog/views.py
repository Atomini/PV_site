from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def index(request):
    production = ProductionCategory.objects.all()
    services = Services.objects.all()
    context = {'production': production, 'services': services, }
    return render(request, 'main/index.html', context)


def by_production_category(request, pk):
    pass


def by_services(request, pk):
    pass


def static_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
