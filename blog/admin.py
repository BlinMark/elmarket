from django.contrib import admin
from .models import Post
from .models import Category, Product, Author
from .models import Order


# Модель автора
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'sername',
                    'phone',
                    'email',
                    'product_format',
                    'product_size',
                    'product',
                    'price',
                    # 'pic'
                    ]


# admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Post)
