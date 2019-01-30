from django.contrib import admin
from user_basket.models import basket, product_data, Shop

admin.site.register(basket)

# class BasketProduct(admin.StackedInline):
#     model = models.
#     extra = 3
#
#
# class OrderDataAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['user']}),
#         ('Shop', {'fields': ['ordered_from_shop']}),
#     ]
#     inlines = [OrderProduct]
#
#
# admin.site.register(models.user_order, OrderDataAdmin)
