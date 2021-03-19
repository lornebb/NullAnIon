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
        revisions = request.POST['revisions']
        reference_link_type = request.POST['reference_link_type']
        reference_link = request.POST['reference_link']
        # mix_extras = request.POST['mix_extras']
        total_price = request.POST['total_price']

        order = Mix.objects.create(
            order_type = "Mix",
            package_type=package_type,
            deliver_by=deliver_by,
            stem_choices=stem_choices,
            revisions=revisions,
            reference_link_type=reference_link_type,
            reference_link=reference_link,
            # mix_extras=mix_extras,
            total_price=total_price,
        )

        context = {
            'order': order,
        }

        messages.success(request, f"Successfully added your \
                            {order.order_type} order to the basket.")

        template = 'checkout/checkout.html'
        return render(request, template, context)
    
    # if a GET (or any other method) we'll create a blank form
    else:
        template = 'services/services.html'
        if request.GET.get("type") == "mix":
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
            production_form = ProductionForm()
            form_title = "Production"
            production_order_type = "Production Order"

            context = {
            'production_form': production_form,
            'form_title': form_title,
            'production_order_type': production_order_type,
            }

            return render(request, template, context)
