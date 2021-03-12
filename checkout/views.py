from django.shortcuts import render, redirect
# reverse
from django.contrib import messages
from services.forms import Mix, Master, Production

from .forms import OrderForm 


def checkout(request):
    
    # order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        
    }

    return render(request, template, context)

def checkout_order(request):
    """ view to get completed order forms to checkout for payment """

    if request.method == 'POST':
        product_obj = Mix(request.POST)
        product = product_obj
        url = 'checkout/checkout.html'
        messages.success(request, f"Successfully added a '{product_obj.order_type}' order to the basket.")

        context = {
            'product' : product,
        }

        return render(request, url, context)
    else: 
        messages.error(request, "You have not filled an order form from services")
        return redirect('home')

