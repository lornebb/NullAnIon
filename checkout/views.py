from django.shortcuts import render, redirect
# reverse
from django.contrib import messages
from services.forms import Mix, Master, Production

from .forms import OrderForm 


def checkout(request):
    
    # order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        # 'order_form': order_form,
    }

    return render(request, template, context)

def checkout_order(request):
    """ view to get completed order forms to checkout for payment """

    if request.method == 'POST':
        product = Mix(request.POST)
        url = 'checkout/checkout.html'
        messages.success(request, f"Successfully added a '{product.order_type}' order to the basket.")
        print(f"CHECKOUT ORDER MADE {product.order_type} *************")
        context = {
            'product=id' : product.id,
        }
        return render(request, url, context)
    else: 
        messages.error(request, "You have not filled an order form from services")
        return redirect('home')

