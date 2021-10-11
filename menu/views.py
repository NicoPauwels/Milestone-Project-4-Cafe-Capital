from django.shortcuts import render
from .models import Item

# Create your views here.

def all_items(request):
    """A view to return all items, including filtering"""

    items = Item.objects.all()

    context = {
        'items': items,
    }
    
    return render(request, 'menu/menu.html', context)