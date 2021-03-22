from django.contrib import admin
from .models import Order


# class OrderLineItemAdminInline(admin.TabularInline):
#     model = OrderLineItem
#     readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_total',
                    'grand_total', 'order_number')
    
    fields = ('order_number', 'order_id', 'product_ordered',
                'full_name', 'email',
                'phone_number', 'order_total',
                'grand_total')
    
    list_display = ('order_number', 'product_ordered',
                    'full_name', 'email',
                    'phone_number', 'order_total',
                    'grand_total')
    
    # ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
