
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Адрес категории')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория'
    )

    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Адрес товара')
    description = models.TextField(verbose_name='Описание')

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )

    available = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants',
        verbose_name='Товар'
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Вариант'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )

    available = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    def __str__(self):
        return f'{self.product.name} — {self.name}'

    class Meta:
        verbose_name = 'Вариант товара'
        verbose_name_plural = 'Варианты товаров'
