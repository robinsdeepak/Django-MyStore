from django.contrib import admin
from user_basket import models


class BasketProduct(admin.StackedInline):
    model = models.basket_product
    extra = 3


class BasketDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
    ]
    inlines = [BasketProduct]


admin.site.register(models.basket, BasketDataAdmin)
