from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import ItemForm


def all_items(request):
    """ A view to return all items per category """

    allitems = Item.objects.all()

    suggestions = allitems.filter(category=1)
    sharings = allitems.filter(category=2)
    for_the_kids = allitems.filter(category=3)
    bistro = allitems.filter(category=4)
    brunch = allitems.filter(category=5)
    dessert = allitems.filter(category=6)
    draft_beer = allitems.filter(category=7)
    in_a_bottle = allitems.filter(category=8)
    aperitivo = allitems.filter(category=9)
    spirits = allitems.filter(category=10)
    premium_cocktails = allitems.filter(category=11)
    hotdrinks = allitems.filter(category=12)
    colddrinks = allitems.filter(category=13)
    digestive = allitems.filter(category=14)
    bubbles = allitems.filter(category=15)
    housewine = allitems.filter(category=16)
    whitewinesuggestions = allitems.filter(category=17)
    redwinesuggestions = allitems.filter(category=18)
    rosewinesuggestions = allitems.filter(category=19)

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


def menu_item(request, item_id):
    """ A view to show an individual item """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'menu/menu_item.html', context)

@login_required
def add_item(request):
    """ Add an item to the menu """
    if not request.user.is_superuser:
        messages.error(request, 'No authorization')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Item was added successfully')
            return redirect(reverse('menu_item', args=[item.id]))
        else:
            messages.error(request, 'Failed to add the item')
    else:
        form = ItemForm()

    template = 'menu/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_item(request, item_id):
    """ Edit an item of the menu """
    if not request.user.is_superuser:
        messages.error(request, 'No authorization')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item successfully updated')
            return redirect(reverse('menu_item', args=[item.id]))
        else:
            messages.error(request, 'Failed to update item')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'menu/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)

@login_required
def delete_item(request, item_id):
    """ Delete a product from the menu """
    if not request.user.is_superuser:
        messages.error(request, 'No authorization')
        return redirect(reverse('home'))
        
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted')
    return redirect(reverse('view_items'))