from django.shortcuts import render, render_to_response
from main.models import *




def index(request):
	return render_to_response('index.html')

def catalog(request):
	cs = Category.objects.all()
	return render_to_response('category.html', context={'categories' : cs})

def product_list(request, category_id):
	ps = Product.objects.filter(category__id=category_id)
	return render_to_response('product_list.html', context={'products' : ps,  'category_id':category_id})

def product(request, category_id, product_id):
	prod = Product.objects.get(id=product_id)
	return render_to_response('product.html', context={'product':prod})

# Custom filters


