from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('production/<slug:slug>', by_production, name='by_production'),
    path('services/<slug:slug>', by_services, name='by_services'),
    path('<str:page>/', static_page, name='static'),
    path('production/rezervuar/<slug:slug>', tank_detail, name='rezervyar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)