from django.db import models


class all_orders(models.Model):
    orders_data = [{'date': '[product_ids]'}]

    def query_string(self):
        return self.orders_data[:10]
