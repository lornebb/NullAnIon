import uuid

from django.db import models
from django.db.models import Sum

# from services import order? 


class Order(models.Model):

    MIX = 'MIX'
    MASTER = 'MASTER'
    PRODUCT_CHOICES = [(MIX, 'Mix'),
                    (MASTER, 'Master'),]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    product_ordered = models.CharField(max_length=6, choices=PRODUCT_CHOICES, blank=False, null=False, default=MIX)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def _generate_order_number(self):
        """
        generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        adding moms at the end to the grand total.
        """
        moms = 0.25

        def percentage(percent, whole):
            return (percent * whole) / 100.0

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total_sum']
        self.grandtotal = (percentage(moms, self.order_total)) + self.order_total
        self.save()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't already been set.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ for mix and master only """

    MIX = 'MIX'
    MASTER = 'MASTER'
    PRODUCT_CHOICES = [(MIX, 'Mix'),
                    (MASTER, 'Master'),]

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product_ordered = models.CharField(max_length=6, choices=PRODUCT_CHOICES, blank=False, null=False, default=MIX)
    due_date = models.DateTimeField(auto_now_add=False)
    references = models.CharField(max_length=1028, null=True, blank=True)
    stems = models.DecimalField(max_digits=2, decimal_places=0, null=False, blank=False)
    revisions = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)
    extras = models.CharField(max_length=2056, null=True, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
            """
            Override the original save method to set the order number
            if it hasn't already been set.
            """
            self.lineitem_total = self.product.price * self.quanity
            super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
