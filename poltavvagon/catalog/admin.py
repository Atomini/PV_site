from django.contrib import admin
from .models import *


class AdditionalTankImageInline(admin.TabularInline):
    model = AdditionalTankImage


class AdditionalTankWagonImageInline(admin.TabularInline):
    model = AdditionalTankWagonImage


class AdditionalServicesImageInline(admin.TabularInline):
    model = AdditionalServicesImage


class AdditionalOtherProductionImageInline(admin.TabularInline):
    model = AdditionalOtherProductionImage


class ProductionCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


class MainBannerAdmin(admin.ModelAdmin):
    pass


class TankAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    inlines = (AdditionalTankImageInline,)


class TransportedCargoAdmin(admin.ModelAdmin):
    pass


class TankWagonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (AdditionalTankWagonImageInline,)


class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_services',)}
    inlines = (AdditionalServicesImageInline,)


class OtherProductionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (AdditionalOtherProductionImageInline,)


admin.site.register(OtherProduction, OtherProductionAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ProductionCategory, ProductionCategoryAdmin)
admin.site.register(MainBanner, MainBannerAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(TransportedCargo, TransportedCargoAdmin)
admin.site.register(TankWagon, TankWagonAdmin)

# Register your models here.
