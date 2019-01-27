from django.db import models

from user.models import UserProfile
from product.models import product_data
from shop.models import Shop


class basket(models.Model):
    class Meta:
        verbose_name = 'User_Basket'
        db_table = 'User_Basket'

    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    basket_product = models.ForeignKey(product_data, on_delete=models.CASCADE)
    basket_product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    numeber_of_items = models.IntegerField()
    products = {'product_id': 'date_added'}

    def query_set(self):
        return self.products[:10]

    def __str__(self):
        return self.userprofile.name + "'s Basket"
