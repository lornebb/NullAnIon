from django.shortcuts import render, redirect
# reverse
from django.contrib import messages
from services.forms import Mix, Master, Production

from .forms import OrderForm 


# def checkout(request):
    
#     template = 'checkout/checkout.html'
#     context = {
#         'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
#         'client_secret': 'test client secret',
#     }

#     return render(request, template, context)

def checkout_order(request):
    """ view to get completed order forms to checkout for payment """
    
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key' : 'pk_test_51IUIt7Bd6jpXBf7R5NJahCpqoKjVCbL0HhAdV06VT8rfFl0SjiJ1UevCn3NLU9sFOfKwulY7du9TMjuEKg0yO0MG001jhrqs7a',
        'client_secret': 'test client secret',
        }

    if request.method == 'POST':
        product_obj = Mix(
        #     request.POST,
        #     initial={
        #         'order_type': 'Mix'
        #     },
        )
        product = product_obj
        messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")

        context = {
            'product' : product,
        }

        return render(request, template, context)
    else:
        messages.error(request, "You have not filled an order form from services")
        return render(request, template, context)
