from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


from .models import *


def index(request):
    banner = MainBanner.objects.all()
    production_category = ProductionCategory.objects.all()
    services = Services.objects.all()
    context = {'banners': banner, 'production_category': production_category, 'services': services}
    return render(request, 'main/index.html', context=context)


def by_production(request, slug):
    category = ProductionCategory.objects.get(slug=slug)
    category_items = Tank.objects.filter(is_active=True, product_category=category.id)

    if slug == 'rezervuaryi':
        template = 'main/category_tank.html'
    elif slug == 'vagonyi':
        template = 'main/category_vagon.html'
    else:
        template = 'main/category_other.html'
    context = {'category': category, 'category_items': category_items}
    return render(request, template_name=template, context=context)


def tank_detail(request, slug):
    tank = Tank.objects.get(slug=slug)

    additional_image = AdditionalTankImage.objects.filter(tank_id=tank.id)
    context = {"tank": tank, 'additional_image': additional_image, }
    return render(request, 'main/tank.html', context=context)


def by_services(request, slug):
    service = Services.objects.get(is_active=True, slug=slug)
    context = {'service': service, }
    return render(request, 'main/service.html', context=context)


def static_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
