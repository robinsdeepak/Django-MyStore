from django.contrib.auth.models import User
from django.db import models
from product.models import product_data
from shop.models import Shop


class BasketManager(models.Manager):

    def all_products(self):
        return 'anything'


class basket(models.Model):
    class Meta:
        verbose_name = 'User Basket'
        db_table = 'User_Basket'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.user.first_name:
            return self.user.first_name + "'s Basket"
        else:
            return self.user.username + "'s Basket"

    @property
    def total_amount(self):
        return sum([(product_set.basket_product.price * product_set.quantity)
                    for product_set in self.basket_product_set.all()])


class basket_product(models.Model):

    basket_obj = models.ForeignKey(basket, on_delete=models.CASCADE)
    basket_product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    basket_product = models.ForeignKey(product_data, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'Basket Items'




