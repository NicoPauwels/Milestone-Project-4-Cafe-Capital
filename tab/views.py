from django.shortcuts import redirect, reverse, HttpResponse
from django.contrib import messages

from menu.models import Item
from menu.views import all_items

# Create your views here.

def add_to_tab(request, item_id):
    """ Add quantity of the specified item to the tab """

    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    tab = request.session.get('tab', {})

    if item_id in list(tab.keys()):
        tab[item_id] += quantity
        messages.success(request, f'Added {quantity} x {item.name} to your tab')
    else:
        tab[item_id] = quantity
        messages.success(request, f'Added {quantity} x {item.name} to your tab')

    request.session['tab'] = tab
    return redirect(redirect_url)


def adjust_tab(request, item_id):
    """ Adjust specified quantity of the specified item in the tab """

    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    tab = request.session.get('tab', {})

    if quantity > 0:
        tab[item_id] = quantity
        messages.success(request, f'Updated {item.name} quantity to {quantity} in your tab')
    else:
        tab.pop(item_id)
        messages.success(request, f'Removed {item.name} from your tab')

    request.session['tab'] = tab
    return redirect(reverse(all_items))


def remove_from_tab(request, item_id):
    """ Remove item from the tab """

    try:
        item = Item.objects.get(pk=item_id)
        tab = request.session.get('tab', {})

        tab.pop(item_id)
        messages.success(request, f'Removed {item.name} from your tab')

        request.session['tab'] = tab
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
