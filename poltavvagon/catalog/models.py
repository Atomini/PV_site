from django.db import models
from .untilities import get_timestamp_path


# Create your models here.

class MainBanner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Подпись баннера')
    url = models.URLField(verbose_name='Ссылка')
    image = models.ImageField(verbose_name='Изображение баннера', blank=False, upload_to=get_timestamp_path)
    is_active = models.BooleanField(verbose_name='Активен?')


class ProductionCategory(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название продукции')

    def __str__(self):
        return self.category_name


class Tank(models.Model):
    tank_name = models.CharField(max_length=200, verbose_name='Название резервуара')
    working_medium = models.TextField(verbose_name='Рабочая среда')
    nominal_volume = models.CharField(max_length=10, verbose_name='Объем номинальной, м3')
    tank_diameter = models.SmallIntegerField(verbose_name='Диаметр резервуара, мм')
    tank_length = models.SmallIntegerField(verbose_name='Длина резервуара, мм')
    tank_height = models.SmallIntegerField(verbose_name='Высота резервуаров, мм')
    max_operating_temperature = models.IntegerField(verbose_name='максимальная рабочая температура')
    min_operating_temperature = models.IntegerField(verbose_name='минимальна рабочая температура')
    working_pressure = models.FloatField(verbose_name='Рабочее давление, МПа')
    seismicity = models.SmallIntegerField(verbose_name='Сейсмичность')
    climatic_performance = models.CharField(max_length=20, verbose_name='Климатическое исполнение')
    product_category = models.ForeignKey(ProductionCategory, on_delete=models.CASCADE, verbose_name='Категория',
                                         null=False)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    poster_image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Главное изображение')
    slider_image = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                     verbose_name='Дополнительные изображение')

    def __str__(self):
        return self.tank_name


class TransportedCargo(models.Model):
    cargo_name = models.CharField(max_length=100, verbose_name='Наименование груза')
    code_ETSNG = models.CharField(max_length=10, verbose_name='Код ЕТСНГ')
    number_OON = models.CharField(max_length=20, blank=True, verbose_name='код ООН')

    def __str__(self):
        return self.cargo_name


class TankWagon(models.Model):
    tank_wagon_name = models.CharField(max_length=200, verbose_name='Название резервуара')
    load_capacity = models.FloatField(verbose_name='Грузоподъемность')
    max_tare_weight = models.FloatField(verbose_name='максимальная масса тары')
    min_tare_weight = models.FloatField(verbose_name='минимальная масса тары')
    boiler_volume = models.CharField(max_length=20, verbose_name='Объем котла')
    static_load = models.CharField(max_length=30, verbose_name='Максимальная расчетная статистическая нагрузка от '
                                                               'колесной пары на рельсы ')
    dimension = models.CharField(max_length=20, verbose_name='Габарит')
    track_width = models.SmallIntegerField(verbose_name='Ширина колеи')
    transport_cargo = models.ForeignKey(TransportedCargo, on_delete=models.PROTECT, verbose_name='перевозимый груз')
    poster_image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Главное изображение')
    slider_image = models.ImageField(blank=True, upload_to=get_timestamp_path,
                                     verbose_name='Дополнительные изображение')
    product_category = models.ForeignKey(ProductionCategory, on_delete=models.CASCADE, verbose_name='Категория',
                                         null=False)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')

    def __str__(self):
        return self.tank_wagon_name
