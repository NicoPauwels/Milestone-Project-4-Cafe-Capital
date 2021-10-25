from django.shortcuts import redirect, reverse

# Create your views here.

def add_to_tab(request, item_id):
    """ Add quantity of the specified item to the tab """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    tab = request.session.get('tab', {})

    if item_id in list(tab.keys()):
        tab[item_id] += quantity
    else:
        tab[item_id] = quantity

    request.session['tab'] = tab
    return redirect(redirect_url)


def adjust_tab(request, item_id):
    """ Adjust specified quantity of the specified item in the tab """

    quantity = int(request.POST.get('quantity'))
    tab = request.session.get('tab', {})

    if quantity > 0:
        tab[item_id] = quantity
    else:
        tab.pop[item_id]

    request.session['tab'] = tab
    return redirect(reverse('all_items'))