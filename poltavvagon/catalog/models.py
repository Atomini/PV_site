from django.db import models
from .untilities import get_timestamp_path
from pytils.translit import slugify


# -------------- Модели для основного баннера ------------
class MainBanner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Подпись баннера')
    url = models.URLField(verbose_name='Ссылка')
    image = models.ImageField(verbose_name='Изображение баннера', blank=False, upload_to=get_timestamp_path)
    is_active = models.BooleanField(verbose_name='Активен?')
    body = models.TextField(verbose_name='Описание', blank=True, max_length=250)
    index = models.IntegerField(verbose_name='Индекс', blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'


# -------------- Модель для продукции ------------
class ProductionCategory(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название продукции')
    prev_text = models.TextField(verbose_name='Основной текст', max_length=250, blank=True)
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение превю', blank=True)
    slug = models.SlugField(auto_created=True, blank=False, unique=True)
    text = models.TextField(verbose_name='Текст на странице', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'


# -------------- Модели для  другой продукции  ------------
class OtherProduction(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    prev_text = models.TextField(max_length=600, verbose_name='Текст превю', blank=True)
    poster_image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Главное изображение')
    description = models.TextField(blank=False, verbose_name='Описание')
    characteristic = models.TextField(blank=True, verbose_name='Характиристики')
    product_category = models.ForeignKey(ProductionCategory, on_delete=models.CASCADE, verbose_name='Категория',
                                         null=False)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    slug = models.SlugField(auto_created=True, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Другая продукция'
        verbose_name_plural = 'Другая продукция'


class AdditionalOtherProductionImage(models.Model):
    production = models.ForeignKey(OtherProduction, on_delete=models.CASCADE, verbose_name='Продукция')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение для слайдера'
        verbose_name_plural = 'Изображения для слайдера'


# -------------- Модели для резервуара ------------
class Tank(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название резервуара')
    prev_text = models.TextField(max_length=600, verbose_name='Текст превю', blank=True)
    poster_image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Главное изображение')

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
    description = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    slug = models.SlugField(auto_created=True, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Резервуар'
        verbose_name_plural = 'Резервуары'


class AdditionalTankImage(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, verbose_name='Резервуар')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение для слайдера'
        verbose_name_plural = 'Изображения для слайдера'


# -------------- Модели для вагона ------------
class TransportedCargo(models.Model):
    cargo_name = models.CharField(max_length=100, verbose_name='Наименование груза')
    code_ETSNG = models.CharField(max_length=10, verbose_name='Код ЕТСНГ')
    number_OON = models.CharField(max_length=20, blank=True, verbose_name='код ООН')

    def __str__(self):
        return self.cargo_name

    class Meta:
        verbose_name = 'Перевозимый груз'
        verbose_name_plural = 'Перевозимык грузы'


class TankWagon(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название резервуара')
    prev_text = models.TextField(max_length=600, verbose_name='Текст превю', blank=True)
    poster_image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Главное изображение')

    load_capacity = models.FloatField(verbose_name='Грузоподъемность')
    max_tare_weight = models.FloatField(verbose_name='максимальная масса тары')
    min_tare_weight = models.FloatField(verbose_name='минимальная масса тары')
    boiler_volume = models.CharField(max_length=20, verbose_name='Объем котла')
    static_load = models.CharField(max_length=30, verbose_name='Максимальная расчетная статистическая нагрузка от '
                                                               'колесной пары на рельсы ')
    dimension = models.CharField(max_length=20, verbose_name='Габарит')
    track_width = models.SmallIntegerField(verbose_name='Ширина колеи')
    transport_cargo = models.ForeignKey(TransportedCargo, on_delete=models.PROTECT, verbose_name='перевозимый груз')
    product_category = models.ForeignKey(ProductionCategory, on_delete=models.CASCADE, verbose_name='Категория',
                                         null=False)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    slug = models.SlugField(auto_created=True, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вагон цистерна'
        verbose_name_plural = 'Вагоны цистерны'


class AdditionalTankWagonImage(models.Model):
    tank = models.ForeignKey(TankWagon, on_delete=models.CASCADE, verbose_name='Вагон-цистерна')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение для слайдера'
        verbose_name_plural = 'Изображения для слайдера'


# -------------- Модели для услуг ------------
class Services(models.Model):
    name_services = models.CharField(max_length=100, verbose_name='Услуги')
    video_link = models.URLField(verbose_name='Видео')
    main_text = models.TextField(verbose_name='Основной текст')
    article = models.CharField(max_length=250, verbose_name='Текст превю')
    slug = models.SlugField(auto_created=True, blank=False, null=True, unique=True)
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение превю', blank=True)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')

    def __str__(self):
        return self.name_services

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class AdditionalServicesImage(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуги')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='изображение')

    class Meta:
        verbose_name = 'Изображение для слайдера'
        verbose_name_plural = 'Изображения для слайдера'
