# from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MixOrderForm, MasterOrderForm, ProductionOrderForm

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

def example_form(request):
    """a view to render example form"""

    mix_order_form = MixOrderForm()
    master_order_form = MasterOrderForm()
    production_order_form = ProductionOrderForm()

    context = {
        'mix_order_form' : mix_order_form,
        'master_order_form' : master_order_form,
        'production_order_form': production_order_form,
    }

    return render(request, 'services/mix.html', context)
                        