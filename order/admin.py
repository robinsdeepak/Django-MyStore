from django.contrib import admin
from . import models


class OrderProduct(admin.StackedInline):
    model = models.user_order_products
    extra = 3


class OrderDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Shop', {'fields': ['ordered_from_shop']}),
    ]
    inlines = [OrderProduct]


admin.site.register(models.user_order, OrderDataAdmin)

