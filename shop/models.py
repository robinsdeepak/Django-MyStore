from django.db import models
from django.contrib.auth.models import User
from product.models import product_data
from .model_options import states
from django.urls import reverse


class Shop(models.Model):
    title = models.CharField(max_length=50)

    # Communication Fields
    # phone = models.IntegerField()
    # email = models.EmailField()

    # Address Fields
    address_line_1 = models.CharField(max_length=200)   # Street name
    address_line_2 = models.CharField(max_length=100, null=True)   # City name
    address_State = models.CharField(max_length=20, choices=states)
    location = models.CharField(max_length=100)     # GPS location

    # About Shop
    about = models.CharField(max_length=500)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    Shop_icon = models.ImageField(verbose_name='Shop Photo 1')
    Shop_icon_2 = models.ImageField(verbose_name='Shop Photo 2', null=True)
    number_of_reviews = models.IntegerField(default=0)

    def add_review(self, new_rating, comment):

        shop = self
        new_rating_obj = review(shop=shop, rating=new_rating, comment=comment)
        new_rating_obj.save()

        shop.rating = (shop.number_of_reviews * float(shop.rating) + new_rating) / (shop.number_of_reviews + 1)
        shop.number_of_reviews += 1
        shop.save()

    def get_absolute_url(self):
        return reverse('Shop: shop-list')

    def __str__(self):
        return self.title


class product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    shop_product = models.ForeignKey(product_data, on_delete=models.CASCADE)
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.shop_product.name


class review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # review can be added in only if user is logged in, and after shopping from the Shop.
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)      # max_value = 5
    comment = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.rating) + "  -  " + str(self.comment)[:10]
