from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('production/<int:pk>', by_production_category, name='by_production'),
    path('services/<int:pk>', by_services, name='by_services'),
    path('<str:page>/', static_page, name='static'),

]