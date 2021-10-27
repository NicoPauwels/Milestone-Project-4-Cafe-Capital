from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from checkout.models import OrderLineItem

from .forms import OrderForm
from .models import Order, OrderLineItem
from menu.models import Item
from tab.context import tab_content

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        tab = request.session.get('tab', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            for item_id, quantity in tab.items():
                try:
                    item = get_object_or_404(Item, pk=item_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            item=item,
                            item_quantity=quantity,
                        )
                    order_line_item.save()
                except Item.DoesNotExist:
                    messages.error(request, 'One of the products in the bag was not found in our database')
                    order.delete()
            
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form')

    else:
        tab = request.session.get('tab', {})
        if not tab:
            messages.error(request, "There's nothing on your tab at the moment")

        current_tab = tab_content(request)
        total = current_tab['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')


    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """" Handle successful checkouts """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order was successfully placed')

    if 'tab' in request.session:
        del request.session['tab']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)