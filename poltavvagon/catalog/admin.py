from django.contrib import admin
from .models import *


class ProductionCategoryAdmin(admin.ModelAdmin):
    pass


class MainBannerAdmin(admin.ModelAdmin):
    pass


class TankAdmin(admin.ModelAdmin):
    pass


class TransportedCargoAdmin(admin.ModelAdmin):
    pass


class TankWagonAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductionCategory, ProductionCategoryAdmin)
admin.site.register(MainBanner, MainBannerAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(TransportedCargo, TransportedCargoAdmin)
admin.site.register(TankWagon, TankWagonAdmin)

# Register your models here.
