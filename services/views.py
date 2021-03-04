from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Mix_order_form

def mix_form(request):
    """ A view to return the mix service from services """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Mix_order_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Mix_order_form()

    return render(request, 'services/mix.html', {'form': form})