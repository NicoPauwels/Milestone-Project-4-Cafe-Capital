from django.shortcuts import get_object_or_404
from menu.models import Item


def show_tab(request):

    tab_items = []
    total = 0
    item_count = 0
    tab = request.session.get('tab', {})

    for item_id, quantity in tab.items():
        item = get_object_or_404(Item, pk=item_id)
        item_total = quantity * item.price
        total += quantity * item.price
        item_count += quantity
        tab_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item_total': item_total,
            'item': item,
        })

    context = {
        'tab_items': tab_items,
        'item_total': item_total,
        'total': total,
        'item_count': item_count,
    }

    return context