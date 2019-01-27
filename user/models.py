from django.db import models
from .model_options import cities_options
from django.urls import reverse


class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.BigIntegerField()   # max_length=10

    def get_absolute_url(self):
        return reverse('user:context-view', self.pk)

    def __str__(self):
        return self.name


class user_address(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, choices=cities_options)  # user will be able to select from options
    area = models.CharField(max_length=50, null=True)
    complete_address = models.CharField(max_length=200, null=True)
    PinCode = models.IntegerField(null=True)          # max_length = 6

    # Temporary Data
    # These data will be completely deleted or will overwrite the existing Data

    ip_address = models.GenericIPAddressField(null=True)    # for address based suggestions
    gps = models.CharField(max_length=30, null=True)   # for address based suggestions and Delivery address

    def __str__(self):
        return self.city + ", " + str(self.PinCode)

