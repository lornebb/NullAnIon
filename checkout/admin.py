from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
   
    readonly_fields = ('order_total',
                    'grand_total',
                    'order_number',
                    'original_bag',
                    'stripe_pid')
    
    # fields = ('order_number',
    #             'full_name',
    #             'email',
    #             'phone_number',
    #             'package_type',
    #             'deliver_by',
    #             'stem_choices',
    #             'revisions',
    #             'reference_link_type',
    #             'reference_link',
    #             'mix_extras',
    #             'contact',
    #             'order_total',
    #             'grand_total',
    #             'original_bag',
    #             'stripe_pid')

    list_display = ('order_number',
                'full_name',
                'email',
                'phone_number',
                'order_total',
                'package_type',
                'deliver_by',
                'stem_choices',
                'revisions',
                'reference_link_type',
                'reference_link',
                'mix_extras',
                'contact',
                'order_total',
                'grand_total',
                'original_bag',
                'stripe_pid')

admin.site.register(Order, OrderAdmin)
