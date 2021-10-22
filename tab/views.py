from django.shortcuts import redirect

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
    print(request.session['tab'])
    return redirect(redirect_url)