from django.shortcuts import render
from django.contrib import messages
# from services.forms import Mix, Master, Production
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import OrderForm
import stripe

# @login_required
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
            for extra in mix_extras:
                print(extra)
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

        # order_form = Order(form_data)
        # if order_form.is_valid():
        messages.success(request, f"Successfully added your \
                    {order_form_services.id} order to the basket.")
        # else:
        # messages.error(request, (f'There was an error with your {order_form} form. '
        #                             'Please double check your information.'))
        
        

        print("order ************************************************************************************************************************************************")
        print(order_form_services.id)
        print("**********************************************************************************************************************************************************")
        
        context = {
            'order_form_to_fill': OrderForm,
            'order_form_services': order_form_services,
            'stripe_public_key': stripe_public_key,
            'stripe_secret_key': stripe_secret_key,
        }

        messages.success(request, f"Successfully added your \
                        {order_form_services.id} order to the basket.")

        template = 'checkout/checkout.html'
        return render(request, template, context)

    else:

        template = 'checkout/checkout.html'
        return render(request, template)


# def checkout_complete(request):
    
#     customer_details = (
#     'order_id': request.POST['order_id'],
#     'full_name': request.POST['full_name'],
#     'email': request.POST['email'],
#     'phone_number': request.POST['phone_number'],
#     )






















    
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
