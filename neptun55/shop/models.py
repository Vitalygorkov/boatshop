from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True, verbose_name='слаг на английском, например "Category"')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Type_boat(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип лодки'
        verbose_name_plural = 'Типы лодок'

class Color(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Boat(models.Model):
    boat_model = models.CharField('Модель', max_length=150) # название
    boat_manufacturer = models.CharField('Производитель',max_length=30) # производитель лодки.
    description = models.TextField('Описание', blank=True) # описание
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField('Цена', blank=True, null=True) # цена

    type_boat = models.ForeignKey(Type_boat, on_delete=models.PROTECT, verbose_name='Тип лодки') # тип лодки гребная или моторная
    TYPE_MOTORS = (
        ('VINT', 'Винт'),
        ('VODOMET', 'Водомет'),
        ('NET', 'Нет'),
    )
    type_motor = models.CharField("Тип мотора", max_length=7, choices=TYPE_MOTORS, blank=True) # вид мотора водомет или винт
    # transom =  # транец  Вклеенный,Крепление под навесной,Нет
    # floor =  # Надувное днище низкого давления,Надувное многобаллонное высокого давления,ПВХ,ПВХ+разборный пайол
    # series =  # серия, модельный ряд
    color = models.CharField("Цвет лодки", max_length=10, blank=True) # цвет
    length = models.IntegerField("Длинна см", blank=True,null=True) # длинна
    width = models.IntegerField("Ширина см", blank=True,null=True) # ширина
    cockpit_length = models.IntegerField("Длинна кокпита см", blank=True,null=True) # длинна кокпита см
    cockpit_width = models.IntegerField("Ширина кокпита см", blank=True, null=True) # ширина кокпита см
    cylinder_diameter = models.IntegerField("Диаметр баллонов см", blank=True, null=True) # Диаметр баллонов см
    inflatable_compartments = models.IntegerField("Количество надувных отсеков", blank=True, null=True) # Количество надувных отсеков
    load_capacity = models.IntegerField("Грузоподъемность кг", blank=True, null=True) # грузоподъемность кг
    passenger_capacity = models.IntegerField("Пассажировместимость чел", blank=True, null=True) # пассажировместимость чел
    maximum_motor_power = models.IntegerField("Макс мощность мотора лс", blank=True, null=True) # максимальная мощность мотора лс
    boat_weight = models.IntegerField("Вес лодки кг", blank=True, null=True) # вес лодки кг
    complete_set_weight = models.IntegerField("Вес полного комплекта кг", blank=True, null=True) # Вес полного комплекта кг
    bulwark = models.BooleanField("Фальшборт", default=False, blank=True) # фальшборт по дефолту нет.
    payol = models.BooleanField("Пайол", default=False, blank=True) # Пайольная\беспайольная по дефолту да
    keel = models.BooleanField("Киль", default=False, blank=True) # Киль есть\нет, по дефолту нет
    image = models.ImageField('Изображение', upload_to="boats/",blank=True) # фото  https://qna.habr.com/q/218059
    # видео


    def __str__(self):
        return self.boat_model

    class Meta:
        verbose_name = 'Лодка'
        verbose_name_plural = 'Лодки'

class Photo_boat(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="photo/")
    boat = models.ForeignKey(Boat, verbose_name="Лодка", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото лодки"
        verbose_name_plural = "Фото Лодок"