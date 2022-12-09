from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from django.urls import reverse


class CategoryBlog(MPTTModel):
    name = models.CharField("Категория", max_length=255)
    url = models.SlugField(max_length=160, verbose_name='URL на английском, например "Category"', unique=True)
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
        db_table = "category_blog"
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id', 'level')


mptt.register(CategoryBlog, order_insertion_by=['name'])

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

class counter_ip_readers(models.Model):
    ip = models.CharField(max_length=100, unique=True, )

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    short_description = models.TextField("Отрывок для показа в блоге",max_length=500)
    # slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(blank=True)
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField("Основная картинка",upload_to='photo/blog/%Y/%m/%d', blank=True)
    views = models.ManyToManyField(counter_ip_readers, verbose_name='Кол-во уникальных просмотров')
    views_simple = models.IntegerField('Кол-во НЕуникальных просмотров', blank=True, null=True)
    category = models.ForeignKey(CategoryBlog, on_delete=models.PROTECT, related_name='posts',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts',
                                  verbose_name='Ключевые слова, словосочетания')

    def __str__(self):
        return self.title

    def counter_views_simple(self):
        self.views_simple += 1
        self.save()
        return self.views_simple

    def counter(self, req):
        count = counter_ip_readers()
        count.ip = req
        try:
            count.save()
            self.views = count.pk
            self.save()
        except Exception as e:
            self.views.add(counter_ip_readers.objects.filter(ip=req)[0].pk)
            self.views.add()
            self.save()


    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_ad']




