from django.http import HttpResponse

from .models import Order
from services.models import Mix, Master, Production

import json
import time


class StripeWH_Handler:
    """handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
    
    def handle_event(self,event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self,event):
        """
        Handle a payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try: 
                order = Order.objects.get(
                    full_name__iexact=billing_details.full_name,
                    email__iexact=billing_details.full_email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt +=1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.full_name,
                    email=billing_details.full_email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status = 500)
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Created order in webhook',
                status=200
            )
    
    def handle_payment_intent_payment_failed(self,event):
        """
        Handle a payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )
