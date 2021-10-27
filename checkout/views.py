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
        'stripe_public_key': 'pk_test_51JAZk3JTrPqsruCE6fQKocKtuEFHLQC0dIKWVQHfUzn3IFGeazbnvT6reKP8Mb9HwDnn8RSR4jo4woCg6bXRYZY200tNhHOIu5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
