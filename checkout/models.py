import uuid

from django.db import models

from profiles.models import UserProfile


class Order(models.Model):

    MIX = 'MIX'
    MASTER = 'MASTER'
    PRODUCT_CHOICES = [(MIX, 'Mix'),
                       (MASTER, 'Master'),
                       ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_type = models.CharField(max_length=20, default='')
    package_type = models.CharField(max_length=50, default='')
    deliver_by = models.DateField(auto_now_add=False)
    stem_choices = models.CharField(
        max_length=1026, blank=False, null=False, default=6)
    revisions = models.CharField(
        max_length=1026, blank=False, null=False, default=3)
    reference_link_type = models.CharField(
        max_length=1026, blank=True, null=True)
    reference_link = models.URLField(blank=True, null=True)
    mix_extras = models.CharField(max_length=1026, default='none')
    contact = models.EmailField(blank=False, null=False, default='')
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False,
        blank=False, default='')

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


class Order_Production(models.Model):

    PRODUCTION_TYPE = [
        ('guitar', 'Guitar'),
        ('bass', 'Bass'),
        ('synths', 'Synths'),
        ('piano', 'Piano'),
        ('drums', 'Drums'),
        ('track_production', 'Track Production')
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='order_production')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_type = models.CharField(max_length=20, default='Production')
    production_type = models.CharField(max_length=1026, choices=PRODUCTION_TYPE, default='')
    deliver_by = models.DateField(auto_now_add=False)

    reference_link_type = models.CharField(
        max_length=1026, blank=True, null=True)
    reference_link = models.URLField(blank=True, null=True)

    contact = models.EmailField(blank=False, null=False, default='')
    notes = models.CharField(max_length=1080, blank=False, null=False)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False,
        blank=False, default='')

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
