# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from models import Product
# Create your views here.

# class based view to handle the featured from models.product
class ProductFeaturedListView(ListView):
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all().featured()

# class based view to handle to featured from models.product with details

class ProductFeaturedDetailView(DetailView):
	# queryset = Product.objects.all()
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()



# class based view for listing of products
class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context =super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print (context)
	# 	return context

	def get_queryset(self, *args, **kwargs):
		request =self.request
		return Product.objects.all()

# function based view
def product_list_view(request):
	queryset = Product.objects.all()
	context  = {
		'object_list': queryset
	}
	return render(request, "products/list.html", context)

# Slug can be used in the url now for products
class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		# instance = get_object_or_404(Product, slug=slug, active=True)
		try:
			instance = Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist :
			raise Http404("Not found")
		except Product.MultipleObjectsReturned :
			qs = Product.objects.filter(slug=slug, active=True)
			instance = qs.first()
		except:
			raise Http404("Hmmmmm")
		return instance


# class based view for details of the product
class ProductDetailView(DetailView):
	# queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context =super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print (context)
		return context

	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't exist !")
		return instance

# function based view to check if the product exists
def product_detail_view(request, pk=None, *args, **kwargs):
	# instance = Product.objects.get(pk=pk)
	# instance = get_object_or_404(Product, pk=pk)
	# try:
	# 	instance = Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print("no product here")
	# 	raise Http404("Product doesn't exist !")
	# else:
	# 	print("huh?")
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist !")
	# qs = Product.objects.filter(id=pk)
	# # print(qs)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Product doesn't exist")	

	context  = {
		'object': instance
	}
	return render(request, "products/detail.html", context)

