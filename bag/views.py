from django.shortcuts import render, redirect, get_object_or_404
from services.models import Mix, Master, Production
from django.contrib import messages

def view_bag(request):
    """ a view to render the bag contents page """

    return render(request, 'bag/bag.html')


# add form details to this function (replace item_id)
def add_to_bag(request):
    """ add filled out order form to the bag """

    if request.method == 'POST':
        # check for other bag contents
        bag = request.session.get('bag', {})

        # pull out form data
        order_type = request.POST.get('order_type')
        deliver_by = request.POST.get('deliver_by')
        reference_link_type = request.POST.get('reference_link_type')
        reference_link = request.POST.get('reference_link')
        production_type = request.POST.get('production_type')

        if bag != {}:
            bag['items'].append({
                'order_type' : order_type,
                'deliver_by' : deliver_by,
                'reference_link_type' : reference_link_type,
                'reference_link' : reference_link,
                'production_type' : production_type,
            })
        else:
            bag['items'] = []
            bag['items'].append({
                'order_type' : order_type,
                'deliver_by' : deliver_by,
                'reference_link_type' : reference_link_type,
                'reference_link' : reference_link,
                'production_type' : production_type,
            })
        
        # redirect_url = request.POST.get('checkout/checkout.html')
        redirect_url = 'checkout/checkout.html'
        request.session['bag'] = bag
        messages.success(request, f"Successfully added a '{order_type}' order to the basket.")
    else:
        messages.error(request, f"Something went wrong, please try again")
        redirect_url = 'home/index.html'
    return render (request, redirect_url)

    # quantity = int(request.POST.get('order_type'))
    # redirect_url = request.POST.get('redirect_url')
    # bag = request.session.get('bag', {})

    # if order_type in list(bag.keys()):
    #     bag[order_type] = quantity
    # else:
        # bag[order_type] = quantity

    # request.session['bag'] = bag
    # template = 'home/index.html'
    # print(request.session['bag'])
    # return render(request, template)
