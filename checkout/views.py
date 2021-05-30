from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IwqikGYtkIPsRUcOJ3ZIvCsJTsJVipuk0LJwENWYj86HcOW19cwB5OBFfwGOplGNg1TISuNN6qYfHOhVVkoun0S00LPQ3Usfn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
