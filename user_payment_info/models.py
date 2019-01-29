from django.db import models
from user.models import UserProfile


class Payment_Detail(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class DebitCard(models.Model):
    user_payment_detail = models.ForeignKey(Payment_Detail, on_delete=models.CASCADE)
    card_number = models.IntegerField()     # max_length=16
    exp_date = {
        'Month': models.IntegerField(),     # max_length=2     # will be change to select from options
        'Year': models.IntegerField()   # max_length=4
    }
