from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MixForm, MasterForm, ProductionForm

# def mix_form(request):
#     """ A view to return the mix service from services """

#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Mix_order_form(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('#')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         # form = Mix_order_form()
#         example_form = ExampleForm()

#     return render(request, 'services/mix.html', {'example_form': example_form})


def mix_form(request):
    """a view to render the mixform form"""

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        mix_form = MixForm(request.POST)
        # check whether it's valid:
        if mix_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('#')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        mix_form = MixForm()
        template = 'services/services.html'
        context = {
            'mix_form' : mix_form,
        }

    return render(request, template, context)


def master_form(request):
    """a view to render the masterform form"""

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        master_form = MasterForm(request.POST)
        # check whether it's valid:
        if master_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('#')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        master_form = MasterForm()
        template = 'services/services.html'
        context = {
            'master_form' : master_form,
        }

    return render(request, template, context)


def production_form(request):
    """a view to render the productionform form"""

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        Production_form = ProductionForm(request.POST)
        # check whether it's valid:
        if Production_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('#')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        production_form = ProductionForm()
        template = 'services/services.html'
        context = {
            'production_form' : production_form,
        }

    return render(request, template, context)
