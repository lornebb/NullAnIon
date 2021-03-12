# from decimal import Decimal
# from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Mix, Master, Production

def bag_contents(request):

    bag_items = []
    total = 123.32
    product_count = 0
    grand_total = total
    bag = request.session.get('bag', {})

    for order_type, quantity in bag.items():
        # product = get_object_or_404(Production, pk=order_type)
        # if bag.order_type == Mix, Master:
            # total += product.price
        # product_count += quantity
        bag_items.append({
            'order_type' : order_type,
            'quantity' : quantity,
            # 'product' : product,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
