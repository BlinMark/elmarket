from django.db import models
from blog.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=60)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    email = models.CharField(verbose_name='Email', max_length=30)
    street = models.CharField(verbose_name='Улица', max_length=30)
    home = models.CharField(verbose_name='Дом', max_length=30)
    korpus = models.CharField(verbose_name='Корпус', max_length=30, blank=True, null=True)
    flat = models.CharField(verbose_name='Квартира', max_length=30)

    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'
