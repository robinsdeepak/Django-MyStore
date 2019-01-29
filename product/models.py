from django.db import models
from .model_options import category_options, attributes


class product_data(models.Model):
    class Meta:
        verbose_name = "Product"
        db_table = "Products"

    name = models.CharField(max_length=100)     # product name given by the company
    category = models.CharField(max_length=20, choices=category_options)   # A json dict data # Nested
    image_link = models.ImageField(max_length=200)
    type = models.CharField(max_length=30)                          # Common name of the product.
    Brand = models.CharField(max_length=30)
    product_info = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=4, decimal_places=2)    # an expression for rating
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name


class product_attributes(models.Model):

    product = models.ForeignKey(product_data, on_delete=models.CASCADE)
    attr = models.CharField(max_length=20, choices=attributes)
    value = models.CharField(max_length=200)

    def __repr__(self):
        return self.attr













# ================== ForeignKeys Data ========================

    # -----------------  Client Side(Data Entry Operator) ---------------------------
    #

    # ----------------- User side ----------------------------
    # numbers_of_this_item_in_basket = models.ForeignKey(default=0)
    # shops_with_availability = models.nearby_shops.filter(product_id=current_product_id)

    # ------------------ Seller Side ---------------------------
