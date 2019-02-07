from django.db import models
from user.model_options import cities_options
from django.contrib.auth.models import User
from django.urls import reverse


# class UserProfile(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     password = models.CharField(max_length=20)
#     phone = models.BigIntegerField()   # max_length=10
#
#     def get_absolute_url(self):
#         return reverse('user:context-view', self.pk)
#
#     def __str__(self):
#         return self.name


class user_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_default = models.BooleanField(default=False)
    city = models.CharField(max_length=20, choices=cities_options)  # user will be able to select from options
    area = models.CharField(max_length=50, null=True)
    complete_address = models.CharField(max_length=200, null=True)
    PinCode = models.IntegerField(null=True)  # max_length = 6

    # Temporary Data
    # These data will be completely deleted or will overwrite the existing Data

    ip_address = models.GenericIPAddressField(null=True)  # for address based suggestions
    gps = models.CharField(max_length=30, null=True)  # for address based suggestions and Delivery address

    def set_default(self):
        """
        Before setting a address as default,
            set the other  address as no default if exist
        :return:
        """
        all_address = self.user.user_address_set.all()
        for address in all_address:
            if address.is_default:
                address.is_default = False
                address.save()
        self.is_default = True
        self.save()

    def __str__(self):
        return self.city + ", " + str(self.PinCode)









