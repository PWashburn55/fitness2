from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HrKP3IdSEiXg0W30naU5GlCSFLui17Cu8Ci3pms11WXg0RNu8h3UwwH4aO42qweulLpH2yotvZ1jWq5JMAKEB2t00jfZXMQaT',
        'stripe_secret_key': 'sk_test_51HrKP3IdSEiXg0W3HFaEjH3Ak2y95KfK13HqjA0egIzqVHOhPk3HeHbsf7rpbje1dkStGdB4UdRq6W2YsqAzNeHJ00N3CzF1Fm'
   }

    return render(request, template, context)
