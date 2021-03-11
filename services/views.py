from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import MixForm, MasterForm, ProductionForm


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
        form_title = "Mix"
        template = 'services/services.html'
        context = {
            'mix_form' : mix_form,
            'form_title' : form_title,
        }

    # messages.success(request, 'Successfully added product!')
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
        form_title = "Master"
        template = 'services/services.html'
        context = {
            'master_form' : master_form,
            'form_title' : form_title,
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
        form_title = "Production"
        template = 'services/services.html'
        context = {
            'production_form' : production_form,
            'form_title' : form_title,
        }

    return render(request, template, context)
