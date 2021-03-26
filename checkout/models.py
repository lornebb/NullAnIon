import uuid

from django.db import models


class Order(models.Model):

    MIX = 'MIX'
    MASTER = 'MASTER'
    PRODUCT_CHOICES = [(MIX, 'Mix'),
                    (MASTER, 'Master'),]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_type = models.CharField(max_length=20, default='')
    package_type = models.CharField(max_length=50, default='')
    deliver_by = models.DateTimeField(auto_now_add=True)
    stem_choices = models.CharField(max_length=1026, blank=False, null=False, default=6)
    revisions = models.CharField(max_length=1026, blank=False, null=False, default=3)
    reference_link_type = models.CharField(max_length=1026, blank=True, null=True)
    reference_link = models.URLField(blank=True, null=True)
    mix_extras = models.CharField(max_length=1026, default='none')
    contact = models.EmailField(blank=False, null=False, default='')
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def _generate_order_number(self):
        """
        generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

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


# class OrderLineItem(models.Model):
#     """ for mix and master only """

#     MIX = 'MIX'
#     MASTER = 'MASTER'
#     PRODUCT_CHOICES = [(MIX, 'Mix'),
#                     (MASTER, 'Master'),]

#     order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
#     product_ordered = models.CharField(max_length=6, choices=PRODUCT_CHOICES, blank=False, null=False, default=MIX)
#     due_date = models.DateTimeField(auto_now_add=False)
#     references = models.CharField(max_length=1028, null=True, blank=True)
#     stems = models.DecimalField(max_digits=2, decimal_places=0, null=False, blank=False)
#     revisions = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)
#     extras = models.CharField(max_length=2056, null=True, blank=True)
#     lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

#     def save(self, *args, **kwargs):
#             """
#             Override the original save method to set the order number
#             if it hasn't already been set.
#             """
#             self.lineitem_total = self.product.price * self.quanity
#             super().save(*args, **kwargs)

#     def __str__(self):
#         return f'SKU {self.product.sku} on order {self.order.order_number}'
