from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'popular')  # Отображение полей в списке
    list_editable = ('popular',)  # Возможность редактировать популярность прямо в списке

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'order_date')  # Основные поля заказа
    list_filter = ('status',)  # Фильтр по статусу заказа
    ordering = ('-order_date',)  # Сортировка по дате заказа (по убыванию)
