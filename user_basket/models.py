from django.contrib.auth.models import User
from django.db import models
from product.models import product_data
from shop.models import Shop


class BasketManager(models.Manager):

    def all_products(self):
        basket_objects = self.objects.all()
        products_list = [i.basket_product for i in basket_objects]

        products = {
                    'product_id': {
                                    'date_added': '',
                                    'quantity': '',
                                    }}

        return products_list


class basket(models.Model):
    class Meta:
        verbose_name = 'User Basket'
        db_table = 'User_Basket'

    # userprofile = models.ForeignKey(User, on_delete=models.CASCADE)
    basket_product = models.ForeignKey(product_data, on_delete=models.CASCADE)
    basket_product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    #number_of_items = models.IntegerField()
    # new_field = models.CharField(max_length=10)

    manager = BasketManager()

    # def query_set(self):
    #     return '30 products'

    def __str__(self):
        return "Basket"
#
