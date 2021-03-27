from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import OrderForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # This is only for MIX at the moment.

        if 'reference_link' in request.POST:
            reference_link = request.POST['reference_link']
            reference_link_type = request.POST['reference_link_type']
        else:
            reference_link = False
            reference_link_type = False

        if request.POST.getlist('mix_extras') != "":
            mix_extras = request.POST.getlist('mix_extras')
        else:
            mix_extras = None

        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
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


        order_form_complete = Order.objects.create(
            order_type = "Mix",
            full_name=full_name,
            email=email,
            phone_number=phone_number,
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


        pid = request.POST.get('client_secret').split('_secret')[0]
        order_form_complete.stripe_pid = pid
        # order_form_complete.original_bag = json.dumps(bag)

        # messages.success(request, f"Successfully added your \
        #             {order_form_services.id} order to the basket.")

        total = grand_total
        stripe_total = round(float(total) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # order_form_complete = get_object_or_404(Order, Order=id)

        context = {
            # 'order_form_to_fill': OrderForm,
            'order_form_complete': order_form_complete,
            'stripe_public_key': stripe_public_key,
            'stripe_secret_key': stripe_secret_key,
            'client_secret': intent.client_secret,
        }

        messages.success(request, f"Successfully completed order \
                        {order_form_complete.id}. A confirmation \
                        email will be sent to {order_form_complete.email}")
        
        if 'bag' in request.session:
            del request.session['bag']
        
        template = 'checkout/checkout_complete.html'

        # return render(request, template, context)
        return redirect(reverse('checkout_complete', args=[order_form_complete.order_number]), context)
    else:
        order_form_services = request.session['bag']
        print(f"order_form_services **************************************{order_form_services}")
        
        order_total = order_form_services['order_total']
        grand_total = order_total

        total = grand_total
        stripe_total = round(float(total) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        template = 'checkout/checkout.html'
        context = {
            'order_form_services': order_form_services,
            'order_form': OrderForm,
            'stripe_public_key': stripe_public_key,
            'stripe_secret_key': stripe_secret_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)


@login_required
def checkout_complete(request, order_number):
    """
    Handle successful checkouts
    """
    order = Order.objects.get(order_number=order_number)
    context = {
        'order': order,
    }
    print(order)
    template = 'checkout/checkout_complete.html'
    return render(request, template, context)
