from django.contrib import admin
from .models import *


class AdditionalTankImageInline(admin.TabularInline):
    model = AdditionalTankImage


class AdditionalTankWagonImageInline(admin.TabularInline):
    model = AdditionalTankWagonImage


class AdditionalServicesImageInline(admin.TabularInline):
    model = AdditionalServicesImage


class ProductionCategoryAdmin(admin.ModelAdmin):
    pass


class MainBannerAdmin(admin.ModelAdmin):
    pass


class TankAdmin(admin.ModelAdmin):
    inlines = (AdditionalTankImageInline,)


class TransportedCargoAdmin(admin.ModelAdmin):
    pass


class TankWagonAdmin(admin.ModelAdmin):
    inlines = (AdditionalTankWagonImageInline,)


class ServicesAdmin(admin.ModelAdmin):
    inlines = (AdditionalServicesImageInline,)


admin.site.register(Services, ServicesAdmin)
admin.site.register(ProductionCategory, ProductionCategoryAdmin)
admin.site.register(MainBanner, MainBannerAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(TransportedCargo, TransportedCargoAdmin)
admin.site.register(TankWagon, TankWagonAdmin)

# Register your models here.
