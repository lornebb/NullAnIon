# from decimal import Decimal
# from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Mix, Master, Production

def bag_contents(request):

    bag_items = []
    total = 0
    order_count = 0
    grand_total = total
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        # if isinstance(item_data, int):
        order = get_object_or_404(Production, pk=item_id)
        total = item_data * order.price
        order_count += item_data
        bag_items.append({
            'order' : order,
            'item_id' : item_id,
            'quantity' : item_data
        })
        

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'order_count': order_count,
        'grand_total': grand_total,
    }

    return context
