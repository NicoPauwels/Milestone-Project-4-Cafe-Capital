from django.http import HttpResponse


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
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200)
    
    def handle_payment_intent_succeeded(self, event):
        """ Handle a failed payment intent webhook from Stripe """
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200)