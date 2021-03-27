from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, 
    HttpResponse)
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import OrderForm

from profiles.models import UserProfile

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # This is only for MIX at the moment.

        if request.POST['reference_link'] != "":
            reference_link_type = request.POST['reference_link_type']
            reference_link = request.POST['reference_link']
        else:
            reference_link_type = None
            reference_link = None

        if request.POST.getlist('mix_extras') != "":
            mix_extras = request.POST.getlist('mix_extras')
        else:
            mix_extras = None

        package_type = request.POST['package_type']
        deliver_by = request.POST['deliver_by']
        stem_choices = request.POST['stem_choices']
        revisions = request.POST['revisions']
        reference_link_type = reference_link_type
        reference_link = reference_link
        mix_extras = mix_extras
        contact = request.POST['contact']
        order_total = request.POST['order_total']
        grand_total = order_total

        order_form_services = Order.objects.create(
            order_type = "Mix",
            package_type=package_type,
            deliver_by=deliver_by,
            stem_choices=stem_choices,
            revisions=revisions,
            reference_link_type=reference_link_type,
            reference_link=reference_link,
            mix_extras=mix_extras,
            contact=contact,
            order_total=order_total,
        )

        # messages.success(request, f"Successfully added your \
        #             {order_form_services.id} order to the basket.")

        total = grand_total
        stripe_total = round(float(total) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            'order_form_to_fill': OrderForm,
            'order_form_services': order_form_services,
            'stripe_public_key': stripe_public_key,
            'stripe_secret_key': stripe_secret_key,
            'client_secret': intent.client_secret,
        }

        messages.success(request, f"Successfully added your \
                        {order_form_services.id} order to the basket.")

        template = 'checkout/checkout.html'
        return render(request, template, context)
    else:
        order_form_services = request.session['bag']
        print(f"order_form_services **************************************{order_form_services}")
        template = 'checkout/checkout.html'
        context = {
            'order_form_services': order_form_services,
            'order_form': OrderForm,
            'stripe_public_key': stripe_public_key,
            'stripe_secret_key': stripe_secret_key,
        }
        # messages.warning(request, f"something went wrong - checkout/views.py")
        return render(request, template, context)


@login_required
def checkout_complete(request, order_number):
    """
    Handle successful checkouts
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        form_data = {
            'full_name' : request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'package_type': request.POST['package_type'],
            'order_total': request.POST['order_total'],
            'order_number': request.POST['order_id'],
            'grand_total': request.POST['order_total'],
        }
        
        order_form = Order(form_data)
        print("************************************************************************")
        print(f"THIS IS THE ORDER FORM with form data: {form_data}")
        print(f"THIS IS THE ORDER FORM with form data: {Order}")
        print(f"THIS IS THE ORDER FORM: {order_form}")
        print("************************************************************************")

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
        
        total = grand_total
        stripe_total = round(float(total) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not stripe_public_key:
            messages.warning(request, ('Stripe public key is missing. '
                                    'Did you forget to set it in '
                                    'your environment?'))

        order = get_object_or_404(Order, order_number)
        messages.success(request, f'Order ordered! Order number {order_number} will be to {order.email} soon')

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'order_number': order_number,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)
    else:
        context = {}
        template = 'checkout/checkout_success.html'
        return render(request, template, context)






















    
#     template = 'checkout/checkout.html'
#     context = {
#         'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
#         'client_secret': 'test client secret',
#     }

#     return render(request, template, context)

# def checkout(request):
#     print("WE MADE IT TO CHECKOUT *************************************************************************************************")
#     """ view to get completed order forms to checkout for payment """
#    
    
#     template = 'checkout/checkout.html'
#     return render(request, template)

    # if request.method == 'POST':
    #     product_obj = Mix(request.POST)
    #     #     request.POST, initial={'order_type': 'Mix'},)
    #     product = product_obj
    #     messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")
    #     total = product.order_total
    #     stripe_total = round(total * 100)
    #     stripe.api_key = stripe_secret_key
    #     intent = stripe.PaymentIntent.create(
    #         amount=stripe_total,
    #         currency=settings.STRIPE_CURRENCY, 
    #     )

    #     if not stripe_public_key:
    #         messages.warning(request, 'Stripe public key is missing. \
    #             Did you forget to set it in your environment?')
    #     context = {
    #         'product' : product,
    #         'stripe_public_key': stripe_public_key,
    #         'client_secret': intent.client_secret,
    #     }

    #     return render(request, template, context)
    # else:
    #     context = {
            
    #     }
    #     # messages.error(request, "You have not filled an order form from services")
    #     return render(request, template, context)


# def checkout_order_master(request):
#     """ view to get completed order forms to checkout for payment """
    
#     template = 'checkout/checkout.html'
#     context = {
#         'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
#         'client_secret': 'test client secret',
#         }

#     if request.method == 'POST':
#         product_obj = Master(request.POST)
#         #     request.POST, initial={'order_type': 'Mix'},)
#         product = product_obj
#         messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")

#         context = {
#             'product' : product,
#         }

#         return render(request, template, context)
#     else:
#         messages.error(request, "You have not filled an order form from services")
#         return render(request, template, context)


# def checkout_order_production(request):
    # """ view to get completed order forms to checkout for payment """
    
    # template = 'checkout/checkout.html'
    # context = {
    #     'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
    #     'client_secret': 'test client secret',
    #     }

    # if request.method == 'POST':
    #     product_obj = Production(request.POST)
    #     #     request.POST, initial={'order_type': 'Mix'},)
    #     product = product_obj
    #     messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")

    #     context = {
    #         'product' : product,
    #     }

    #     return render(request, template, context)
    # else:
    #     messages.error(request, "You have not filled an order form from services")
    #     return render(request, template, context)
