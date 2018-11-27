# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.views.generic import ListView
from django.shortcuts import render
from products.models import Product

# Create your views here.
# class based view for listing of products
class SearchProductView(ListView):
	# queryset = Product.objects.all()
	template_name = "search/view.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(SearchProductView, self).get_context_data(*args, **kwargs)
	# 	query   = self.request.GET.get('q')
	# 	context['query'] = query

	# 	return context

	# get the search area working with name 'q' using request.GET which is built in
	def get_queryset(self, *args, **kwargs):
		request =self.request
		print(request.GET)
		query = request.GET.get('q', None) 
		print(query)
		if query is not None:
			# distinct removes redundant products if they exist lookups
			return Product.objects.search(query)
		return Product.objects.featured()
		'''
		__icontains = field contains this
		__iexact    = field is exactly this
		
		'''