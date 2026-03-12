from django.db import models
from django.db.models import Count




class ProfileCustomManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(all_orders=Count('orders')).filter(all_orders__gt=2).order_by('-all_orders')