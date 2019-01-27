from django.contrib import admin
from . import models

# admin.site.register(models.Shop)


class ProductInline(admin.StackedInline):
    model = models.product
    extra = 5


class ShopView(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),

        ('Address', {'fields': ['address_line_1', 'address_line_2', 'address_State', 'location']}),
        ('About Shop', {'fields': ['about', 'rating', 'Shop_icon', 'Shop_icon_2']}),

    ]
    inlines = [ProductInline]


admin.site.register(models.Shop, ShopView)
