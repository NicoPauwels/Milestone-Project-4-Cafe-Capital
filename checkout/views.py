from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    tab = request.session.get('tab', {})
    if not tab:
        messages.error(request, "There's nothing on your tab at the moment")
        return redirect(reverse('all_items'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
