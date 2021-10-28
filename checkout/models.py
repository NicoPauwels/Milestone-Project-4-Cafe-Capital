from typing import ItemsView
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from menu.models import Item


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_tab = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


    def _generate_order_number(self):
        """ Generate unique ordernumber with UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update total each time a line is added """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """ Override original save method """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, *kwargs)
    
    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        """ Override original save method """
        self.lineitem_total = self.item.price * self.item_quantity
        super().save(*args, *kwargs)

    def __str__(self):
        return f'{self.item.name} on order {self.order.order_number}'
