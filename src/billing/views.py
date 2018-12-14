# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import stripe
stripe.api_key = ""
STRIPE_PUB_KEY = ''

def payment_method_view(request):
	if request.method == 'POST':
		print(request.POST)
	return render(request, 'billing/payment-method.html', {"publish_key":STRIPE_PUB_KEY})