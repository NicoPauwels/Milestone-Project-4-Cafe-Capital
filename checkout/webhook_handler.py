from django.http import HttpResponse

from .models import Order, OrderLineItem
from menu.models import Item
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler():
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """ Handle a generic/unknow/unexpected webhook event """
        return HttpResponse(
            content = f'Unhandled Webhook received: {event["type"]}',
            status = 200)
   
    def handle_payment_intent_succeeded(self, event):
        """ Handle a succesful payment intent webhook from Stripe """

        intent = event.data.object
        pid = intent.id
        tab = intent.metadata.tab
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.data.charges[0].amount / 100, 2)

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.full_name = billing_details.name
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    order_total=order_total,
                    original_tab=tab,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt +=1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content = f'Webhook received: {event["type"]} | SUCCESS: Order already in database',
                status = 200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    original_tab=tab,
                    stripe_pid=pid,
                )
                for item_id, quantity in json.loads(tab).items():
                    item = Item.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        item_quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content = f'Webhook received: {event["type"]} | SUCCESS: Created order in the webhook',
            status = 200)
    
    def handle_payment_intent_payment_failed(self, event):
        """ Handle a failed payment intent webhook from Stripe """
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200)