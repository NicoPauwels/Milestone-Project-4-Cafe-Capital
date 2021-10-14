from typing import Dict
from django.shortcuts import render
from .models import Category, Item

# Create your views here.

def all_items(request):
    """ A view to return all items per category """

    suggestions = Item.objects.filter(category=1)
    sharings = Item.objects.filter(category=2)
    for_the_kids = Item.objects.filter(category=3)
    bistro = Item.objects.filter(category=4)
    brunch = Item.objects.filter(category=5)
    dessert = Item.objects.filter(category=6)
    draft_beer = Item.objects.filter(category=7)
    in_a_bottle = Item.objects.filter(category=8)
    aperitivo = Item.objects.filter(category=9)
    spirits = Item.objects.filter(category=10)
    premium_cocktails = Item.objects.filter(category=11)
    hotdrinks = Item.objects.filter(category=12)
    colddrinks = Item.objects.filter(category=13)
    digestive = Item.objects.filter(category=14)
    bubbles = Item.objects.filter(category=15)
    housewine = Item.objects.filter(category=16)
    whitewinesuggestions = Item.objects.filter(category=17)
    redwinesuggestions = Item.objects.filter(category=18)
    rosewinesuggestions = Item.objects.filter(category=19)

    context = {
        'suggestions': suggestions,
        'sharings': sharings,
        'for_the_kids': for_the_kids,
        'bistro': bistro,
        'brunch': brunch,
        'dessert': dessert,
        'draft_beer': draft_beer,
        'in_a_bottle': in_a_bottle,
        'aperitivo': aperitivo,
        'spirits': spirits,
        'premium_cocktails': premium_cocktails,
        'hotdrinks': hotdrinks,
        'colddrinks': colddrinks,
        'digestive': digestive,
        'bubbles': bubbles,
        'housewine': housewine,
        'whitewinesuggestions': whitewinesuggestions,
        'redwinesuggestions': redwinesuggestions,
        'rosewinesuggestions': rosewinesuggestions,
    }
    
    return render(request, 'menu/menu.html', context)