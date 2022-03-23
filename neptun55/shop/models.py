from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt




class Category(MPTTModel):
    name = models.CharField("Категория",max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, verbose_name='URL на английском, например "Category"')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        return f'/{self.url}/'
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['-tree_id']
    class Meta:
        db_table = "category"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id','level')

mptt.register(Category, order_insertion_by=['name'])

# class Subcategory(models.Model):
#     name = models.CharField("Подкатегория",max_length=150)
#     description = models.TextField("Описание")
#     url = models.SlugField(max_length=160, verbose_name='слаг на английском, например "Category"')
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'Подкатегория'
#         verbose_name_plural = 'Подкатегории'

class Manufacturer(models.Model):
    name = models.CharField("Производитель",max_length=50)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Color(models.Model):
    name = models.CharField("Цвет", max_length=50, unique= True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Product(models.Model):
    name = models.CharField(max_length=150)
    short_description =  models.CharField(max_length=1000, blank=True)
    description = models.TextField('Описание', blank=True)  # описание
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField('Цена', blank=True, null=True)  # цена
    color = models.ForeignKey(Color, verbose_name= "Цвет", on_delete=models.SET_NULL, null=True, blank= True) # цвет
    # subcategory = models.ForeignKey(Subcategory,on_delete= models.CASCADE)
    # category = models.ForeignKey(Category,blank=True,default=None, on_delete = models.CASCADE)
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, blank=True,null=True,related_name='cat_product')
    slug = models.SlugField(max_length=250,unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# class Type_boat(models.Model):
#     name = models.CharField("Тип лодки", max_length=50)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'Тип лодки'
#         verbose_name_plural = 'Типы лодок'

# class Type_bottom(models.Model):
#     name = models.CharField("Тип дна", max_length=50)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'Тип дна'
#         verbose_name_plural = 'Типы дна'

class Boat(Product):
    # boat_model = models.CharField('Модель', max_length=150, unique= True) # название
    # manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", on_delete=models.SET_NULL, null=True) # производитель лодки.
    # description = models.TextField('Описание', blank=True) # описание
    # category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True) # Категория
    # category = TreeForeignKey(Category, on_delete=models.SET_NULL,blank=True, null=True, related_name='cat_boat', verbose_name='Категория')
    # subcategory = models.ForeignKey(Subcategory, verbose_name="Подкатегория", on_delete=models.SET_NULL, null=True)  # подкатегория


    # type_boat = models.ForeignKey(Type_boat, on_delete=models.PROTECT, verbose_name='Тип лодки') # тип лодки гребная или моторная
    # type_bottom = models.ForeignKey(Type_bottom, on_delete=models.PROTECT, verbose_name='Тип дна')  # тип л

    # TYPE_MOTORS = (
    #     ('VINT', 'Винт'),
    #     ('VODOMET', 'Водомет'),
    #     ('NET', 'Нет'),
    # )
    # type_motor = models.CharField("Тип мотора", max_length=7, choices=TYPE_MOTORS, blank=True) # вид мотора водомет или винт
    # transom =  # транец  Вклеенный,Крепление под навесной,Нет
    # floor =  # Надувное днище низкого давления,Надувное многобаллонное высокого давления,ПВХ,ПВХ+разборный пайол
    # series =  # серия, модельный ряд
    # color = models.ForeignKey(Color, verbose_name= "Цвет лодки", on_delete=models.SET_NULL, null=True, blank= True) # цвет
    length = models.IntegerField("Длинна см", blank=True,null=True) # длинна
    width = models.IntegerField("Ширина см", blank=True,null=True) # ширина
    cockpit_length = models.IntegerField("Длинна кокпита см", blank=True,null=True) # длинна кокпита см
    cockpit_width = models.IntegerField("Ширина кокпита см", blank=True, null=True) # ширина кокпита см
    cylinder_diameter = models.IntegerField("Диаметр борта см", blank=True, null=True) # Диаметр баллонов см
    fabric_thickness_bottom = models.IntegerField("Плотность ткани дна (г/м²)", blank=True, null=True)  # Диаметр
    fabric_thickness_side = models.IntegerField("Плотность ткани борта (г/м²)", blank=True, null=True)  # Диаметр
    inflatable_compartments = models.IntegerField("Количество надувных отсеков", blank=True, null=True) # Количество надувных отсеков
    load_capacity = models.IntegerField("Грузоподъемность кг", blank=True, null=True) # грузоподъемность кг
    passenger_capacity = models.IntegerField("Пассажировместимость чел", blank=True, null=True) # пассажировместимость чел
    maximum_motor_power = models.IntegerField("Макс мощность мотора лс", blank=True, null=True) # максимальная мощность мотора лс
    boat_weight = models.IntegerField("Вес лодки кг", blank=True, null=True) # вес лодки кг
    complete_set_weight = models.IntegerField("Вес полного комплекта кг", blank=True, null=True) # Вес полного комплекта кг
    bulwark = models.BooleanField("Фальшборт", default=False, blank=True) # фальшборт по дефолту нет.
    keel = models.BooleanField("Киль", default=False, blank=True) # Киль есть\нет, по дефолту нет
    upak = models.CharField("Габариты упаковки(Д*Ш*В)", max_length=100,blank=True)
    # image = models.ImageField('Изображение', upload_to="boats/",blank=True) # фото  https://qna.habr.com/q/218059
    # видео

    class Meta:
        verbose_name = 'Лодка'
        verbose_name_plural = 'Лодки'

class Photo_product(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="photo/")
    product = models.ForeignKey(Product, verbose_name="", related_name='prodimg', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="Лодка", related_name='prodreviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class VideosProducts(models.Model):
    video = models.CharField("Ссылка на видеоролик, например https://www.youtube.com/watch?v=QBkUCVVpyGE убрать всё до знака = и оставить QBkUCVVpyGE ", max_length=100)
    product = models.ForeignKey(Product, verbose_name="Товар", related_name='prodvideos',on_delete= models.CASCADE, null=True)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


