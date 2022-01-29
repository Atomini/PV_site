from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def index(request):
    banner = MainBanner.objects.all()
    production_category = ProductionCategory.objects.all()
    services = Services.objects.all()
    context = {'banners': banner, 'production_category': production_category, 'services': services}
    return render(request, 'main/index.html', context=context)


def by_production_category(request, slug):
    pass


def by_services(request, slug):
    pass


def static_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
