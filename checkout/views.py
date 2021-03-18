from django.shortcuts import render, redirect
# reverse
from django.contrib import messages
from services.forms import Mix, Master, Production
from django.conf import settings

from .forms import OrderForm 
import stripe


# def checkout(request):
    
#     template = 'checkout/checkout.html'
#     context = {
#         'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
#         'client_secret': 'test client secret',
#     }

#     return render(request, template, context)

def checkout(request):
    print("WE MADE IT *************************")
    """ view to get completed order forms to checkout for payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    template = 'checkout/checkout.html'


    if request.method == 'POST':
        product_obj = Mix(request.POST)
        #     request.POST, initial={'order_type': 'Mix'},)
        product = product_obj
        messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")
        total = product.total_price
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY, 
        )

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
        context = {
            'product' : product,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)
    else:
        context = {
            
        }
        # messages.error(request, "You have not filled an order form from services")
        return render(request, template, context)


def checkout_order_master(request):
    """ view to get completed order forms to checkout for payment """
    
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
        'client_secret': 'test client secret',
        }

    if request.method == 'POST':
        product_obj = Master(request.POST)
        #     request.POST, initial={'order_type': 'Mix'},)
        product = product_obj
        messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")

        context = {
            'product' : product,
        }

        return render(request, template, context)
    else:
        messages.error(request, "You have not filled an order form from services")
        return render(request, template, context)


def checkout_order_production(request):
    """ view to get completed order forms to checkout for payment """
    
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
        'client_secret': 'test client secret',
        }

    if request.method == 'POST':
        product_obj = Production(request.POST)
        #     request.POST, initial={'order_type': 'Mix'},)
        product = product_obj
        messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")

        context = {
            'product' : product,
        }

        return render(request, template, context)
    else:
        messages.error(request, "You have not filled an order form from services")
        return render(request, template, context)
