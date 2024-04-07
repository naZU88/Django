from django.contrib import admin
from .models import Product, Order, Client


@admin.action(description="Сбросить количество в ноль")
def reset_quant(modeladmin, request, queryset):
    queryset.update(quant=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quant']
    ordering = ['-price']
    list_filter = ['date_add', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quant]
    
    fields = ['name', 'description', 'quant', 'date_add', 'price']
    readonly_fields = ['date_add']


admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)