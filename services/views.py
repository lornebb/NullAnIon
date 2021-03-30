from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MixForm, MasterForm, ProductionForm
from checkout.views import checkout, checkout_production


def production_order(request):
    if request.POST['reference_link'] != "":
        reference_link_type = request.POST['reference_link_type']
        reference_link = request.POST['reference_link']
    else:
        reference_link_type = None
        reference_link = None

    production_type = request.POST.getlist('production_type')
    reference_link_type = reference_link_type
    reference_link = reference_link
    deliver_by = request.POST['deliver_by']
    contact = request.POST['contact']
    notes = request.POST['notes']

    order = {
        'order_type': "Production",
        'production_type': production_type,
        'deliver_by': deliver_by,
        'reference_link_type': reference_link_type,
        'reference_link': reference_link,
        'contact': contact,
        'notes': notes,
    }

    bag = request.session['bag'] = order

    messages.success(request, f"Successfully added your \
                            {bag['order_type']} order to the basket.")

    return redirect(checkout_production)


def order_form(request):
    """a view to render the mixform / masterform or productionform"""

    if request.method == 'POST':
        # This is only for MIX at the moment.

        bag = request.session.get('bag', {})

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
        
        if request.POST.getlist('master_extras') != "":
            mix_extras = request.POST.getlist('master_extras')
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

        order = {
            'order_type': "Mix",
            'package_type': package_type,
            'deliver_by': deliver_by,
            'stem_choices': stem_choices,
            'revisions': revisions,
            'reference_link_type': reference_link_type,
            'reference_link': reference_link,
            'mix_extras': mix_extras,
            'contact': contact,
            'order_total': order_total,
        }

        bag = request.session['bag'] = order

        messages.success(request, f"Successfully added your \
                             {bag['order_type']} order to the basket.")

        return redirect(checkout)

    else:
        template = 'services/services.html'
        if request.GET.get("type") == "mix":
            mix_form = MixForm()
            form_title = "Mix"
            mix_order_type = 'Mix Order'

            context = {
                'mix_form': mix_form,
                'form_title': form_title,
                'mix_order_type': mix_order_type,
            }

            return render(request, template, context)

        if request.GET.get("type") == "master":
            master_form = MasterForm()
            form_title = "Master"
            master_order_type = "Master Order"

            context = {
                'master_form': master_form,
                'form_title': form_title,
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
