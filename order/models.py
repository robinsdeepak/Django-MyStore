from django.db import models
from django.contrib.auth.models import User
from product.models import product_data
from shop.models import Shop
from django.utils import timezone
from order.model_options import numbers
from user import models as user_models


class user_order(models.Model):
    class Meta:
        verbose_name = 'User Order'
        db_table = 'User Order'

    # order_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_from_shop = models.ForeignKey(Shop, verbose_name='Sold by', on_delete=models.PROTECT)

    # shipping_address = models.ForeignKey(user_models.user_address,
    #                                      verbose_name='shipping address',
    #                                      on_delete=models.PROTECT)

    date_ordered = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(null=True, decimal_places=2, max_digits=9)

    def __str__(self):
        return self.user.username + '\'s Order from ' + self.ordered_from_shop.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        x = sum([
            (product.ordered_quantity * product.ordered_product.price)
            for product in self.user_order_products_set.all()
        ])

        self.total_amount = x
        super().save()


# product will have to be grouped in basket.
# !!! Below class should have only one
# instance for one user_order instance
class user_order_products(models.Model):
    class Meta:
        verbose_name = 'Ordered Product'
        verbose_name_plural = 'Ordered Products'
        db_table = 'Ordered Products'

    for_order = models.ForeignKey(user_order, on_delete=models.CASCADE)
    ordered_product = models.ForeignKey(product_data, on_delete=models.PROTECT)

    # ordered quantity will be shown in user order history
    # and quantity_available will decrease from the shop
    ordered_quantity = models.IntegerField(default=1, choices=numbers)
    product_price = models.DecimalField(null=True, max_digits=9, decimal_places=2)

    # Check if promotions are available and applied

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.product_price = self.ordered_product.price * self.ordered_quantity
        super().save()

    def __str__(self):
        return self.for_order.user.username + '\'s Products ordered from ' + self.for_order.ordered_from_shop.title

# 1. Need to find a dictionary like model for the user_order, as this is not the proper way.
#       >> if not model manager can be used to return dictionary like object
#       >> another option is to create a Model Field

# 2. Here user_order can be used as abstract class for user_order_products
#       >> will be better than now. (27.01.2019)
#       >>
#       >>

# 3.
