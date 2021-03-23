from django.contrib import admin
from .models import Order


# class OrderLineItemAdminInline(admin.TabularInline):
#     model = OrderLineItem
#     readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_total',
                    'grand_total',
                    'order_number',)
    
    # fields = ('order_number',
    #             'full_name',
    #             'email',
    #             'phone_number',
    #             'order_total',
    #             'package_type',
    #             'devlier_by',
    #             'stem_choices',
    #             'revisions',
    #             'reference_link_type',
    #             'reference_link',
    #             'mix_extras',
    #             'contact',
    #             'order_total',
    #             'grand_total')
    
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
                'grand_total')
    
    # ordering = ('deliver_by',)

admin.site.register(Order, OrderAdmin)
