from django.shortcuts import render, redirect

def view_bag(request):
    """ a view to render the bag contents page """

    return render(request, 'bag/bag.html')


# add form details to this function (replace item_id)
def add_to_bag(request):
    """ add filled out order form to the bag """

    # quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # if order_type in list(bag.keys()):
    #     bag[order_type] = quantity
    # else:
    #     bag[order_type] = quantity

    request.session['bag'] = bag
    template = 'services/services.html'
    print(request.session['bag'])
    return render(request, template)
