from django.contrib import admin
from . import models


class AttrInline(admin.StackedInline):
    model = models.product_attributes
    extra = 3


class ProductDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Details', {'fields': ['category', 'type', 'Brand', 'price', 'product_info', 'rating', 'image_link'],
                     'classes': ['expand']}),
    ]
    inlines = [AttrInline]


admin.site.register(models.product_data, ProductDataAdmin)

# FlatPageAdmin
