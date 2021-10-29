from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from menu.models import Item
from menu.views import all_items
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from tab.context import tab_content

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'tab': json.dumps(request.session.get('tab', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Your payment can not be processed')
        return HttpResponse(content=e, status=400)


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
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_tab = json.dumps(tab)
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
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form')
            return redirect(reverse(all_items))

    else:
        tab = request.session.get('tab', {})
        if not tab:
            messages.error(request, "There's nothing on your tab at the moment")
            return redirect(reverse(all_items))

        current_tab = tab_content(request)
        total = current_tab['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')
        return redirect(reverse(all_items))


    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """" Handle successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'full_name': order.full_name,
                'email': order.email,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order was successfully placed')

    if 'tab' in request.session:
        del request.session['tab']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)