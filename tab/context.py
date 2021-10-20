def show_tab(request):

    tab_items = []
    total = 0
    item_count = 0

    context = {
        'tab_items': tab_items,
        'total': total,
        'item_count': item_count,
    }

    return context