from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import MixForm, MasterForm, ProductionForm
from .models import Mix, Master, Production


def order_form(request):
    """a view to render the mixform / masterform or productionform"""

    if request.method == 'POST':
        package_type = request.POST['package_type']
        deliver_by = request.POST['deliver_by']
        stem_choices = request.POST['stem_choices']
        total_price = request.POST['total_price']

        order = Mix.objects.create(
            package_type=package_type,
            deliver_by=deliver_by,
            stem_choices=stem_choices,
            total_price=total_price,
        )

        context = {
            'order': order,
        }

        messages.success(request, f"Successfully added a '{order.id}' order to the basket.")

        # product = MixForm(request.POST)
        # master_form = MasterForm(request.POST)
        # if mix_form.is_valid():
        template = 'checkout/checkout.html'
        return render(request, template, context)
        # product=id)

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
