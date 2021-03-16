from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import MixForm, MasterForm, ProductionForm


def order_form(request):
    """a view to render the mixform form"""

    if request.method == 'POST':
        product = MixForm(request.POST)
        master_form = MasterForm(request.POST)
        # if mix_form.is_valid():
        template = 'checkout/checkout.html'
        messages.success(request, f"Successfully added a '{product.order_type}' order to the basket.")
        print(f"CHECKOUT ORDER MADE {product.order_type} *******************************************************************************************")
        return redirect('checkout_order', product=id)

        # # create a form instance and populate it with data from the request:
        # mix_form = MixForm(request.POST)
        # # check whether it's valid:
        # if mix_form.is_valid():
        #     print("Mix Form is valid and this inner function was called *******************************")
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     return HttpResponseRedirect('#')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        template = 'services/services.html'
        # print(request.get("myquery"))
        if request.GET.get("type") == "mix":
            print(f"*******************{type}****** MIX?")
            print(request.GET.get("type"))
            mix_form = MixForm()
            form_title = "Mix"
            mix_order_type = 'Mix Order'

            context = {
            'mix_form' : mix_form,
            'form_title' : form_title,
            'mix_order_type' : mix_order_type,
            }

            return render(request, template, context)

        if request.GET.get("type") == "master":
            print(f"*******************{type}**** MASTER?")
            print(request.GET.get("type"))
            master_form = MasterForm()
            form_title = "Master"
            master_order_type = "Master Order"
            
            context = {
            'master_form' : master_form,
            'form_title' : form_title,
            'master_order_type': master_order_type,
            }

            return render(request, template, context)
        
        if request.GET.get("type") == "production":
            print(f"*******************{type}******* Production?")
            print(request.GET.get("type"))
            production_form = ProductionForm()
            form_title = "Production"
            production_order_type = "Production Order"

            context = {
            'production_form': production_form,
            'form_title': form_title,
            'production_order_type': production_order_type,
            }

            return render(request, template, context)
        
     

    


# def master_form(request):
    # """a view to render the masterform form"""

    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     master_form = MasterForm(request.POST)
    #     # check whether it's valid:
    #     if master_form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('#')
    
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     master_form = MasterForm()
    #     form_title = "Master"
    #     order_type = "Master order"
    #     template = 'services/services.html'
    #     context = {
    #         'master_form' : master_form,
    #         'form_title' : form_title,
    #         'order_type' : order_type
    #     }

    # return render(request, template, context)
