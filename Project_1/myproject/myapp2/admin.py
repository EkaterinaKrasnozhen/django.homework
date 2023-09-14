from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['phone']
    search_help_text = 'Поиск по полю "телефон клиента"(phone)'
    readonly_fields = ['regist']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'amount', 'date']
    ordering = ['date']
    list_filter = ['date']
    search_fields = ['pk']
    search_help_text = 'Поиск по полю "id заказа"'
    readonly_fields = ['date']
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'price']
    ordering = ['rating']
    list_filter = ['add_date', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю "название продукта"(name)'
    actions = [reset_quantity]
    readonly_fields = ['rating', 'add_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
                {
            'classes': ['collapse'],
            'description': 'Описание товара',
            'fields': ['title'],
                },
        ),
        (
            'Бухгалтерия',
                {
            'fields': ['price', 'count'],   
                }
        ),
        (
            'Рейтинг и прочее',
                {
            'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
            'fields': ['rating', 'add_date'],
                }
        ),
    ]

    
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

