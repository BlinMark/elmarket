from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Модель новостей
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name="Название")
    # text = models.TextField()
    text = RichTextUploadingField(config_name='default')  # текстовый редактор
    full_text = RichTextUploadingField(config_name='default')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Пост'
        verbose_name_plural = 'Новости'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Модель автора
class Author(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:ProductListByAuthor', args=[self.slug])


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:ProductListByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", blank=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    # author = models.ForeignKey(Author, related_name='author', verbose_name="Автор")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    # description = models.TextField(blank=True, verbose_name="Описание")
    description = RichTextUploadingField(config_name='default', blank=True,
                                         verbose_name="Описание")  # текстовый редактор
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе", blank=True)
    available = models.BooleanField(default=True, verbose_name="Доступен", blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    date = models.PositiveIntegerField(default='2017', verbose_name="Год", blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:ProductDetail', args=[self.id, self.slug])


class Order(models.Model):
    # pic = models.ImageField(blank=True, help_text='150x150px', verbose_name='LOL')
    price = models.CharField(max_length=100, verbose_name='Цена', blank=True, null=True)
    product = models.CharField(max_length=100, verbose_name='Товар', blank=True, null=True)
    name = models.CharField(max_length=20, verbose_name="Имя", blank=True, null=True)
    sername = models.CharField(max_length=20, verbose_name='Фамилия', blank=True, null=True)
    phone = models.PositiveIntegerField(verbose_name='Телефон', blank=True, null=True)
    email = models.EmailField(max_length=30, verbose_name='E-mail', blank=True, null=True)

    # Формат товара
    picture = 'Картина'
    poster = 'Постер'
    FORMAT = (
        (picture, 'Картина'),
        (poster, 'Постер')
    )
    product_format = models.CharField(max_length=50, verbose_name='Формат', choices=FORMAT, default=0)

    # Размер товара
    # A1 = 'A0 (80*120 см)'
    A2 = 'A1 (60*80 см)'
    A3 = 'A2 (40*60 см)'
    A4 = 'A3 (30*40 см)'
    # A5 = 'A4 (20*30 см)''
    SIZE = (
        # (A1, 'A0 (80*120 см)'),
        (A2, 'A1 (60*80 см)'),
        (A3, 'A2 (40*60 см)'),
        (A4, 'A3 (30*40 см)'),
        # (A5, 'A4 (20*30 см)'),
    )
    product_size = models.CharField(max_length=50, verbose_name='Размер', choices=SIZE, default=A4)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
