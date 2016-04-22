from django.shortcuts import render, render_to_response
from main.models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json



def index(request):
	return render_to_response('index.html')

def catalog(request):
	cs = Category.objects.all()
	return render_to_response('category.html', context={'categories' : cs})

def product_list(request, category_id):
	category = Category.objects.get(id=category_id)
	ps = Product.objects.filter(category__id=category_id)
	return render_to_response('product_list.html', context={'products' : ps,  'category_id':category_id, 'category':category})

def product(request, product_id):
	prod = Product.objects.get(id=product_id)
	user = request.user; 
	return render_to_response('product.html', context={'product':prod,'user':user})

@login_required
def addSpecification(request, id):
	if request.POST:
		product = Product.objects.get(id=id)
		data = json.loads(request.body.decode('utf-8'))
		specs = data['specs']
		fields = data['fields']
		print(fields)
		#parsing json'а сначала все спецификации потом все значения
		for i in range(0, len(specs)):
			new_spec = SpecificationInstance(product=product, index=specs[i], number=i+1)
			new_spec.save()
		for i in range(0, len(fields)):
			new_field = SpecificationField(product=product, title=fields[i]['field'], measure=fields[i]['measure'])
			new_field.save()

			for j in range(0, len(fields[i]['values'])):
				
				print(SpecificationInstance.objects.filter(index=fields[i]['values'][j]['specification'])[0].id)
				new_specification_value = SpecificationInstanceValue(specification_field=new_field, specification_instance=SpecificationInstance.objects.filter(index=fields[i]['values'][j]['specification'])[0], value=fields[i]['values'][j]['value'])
				new_specification_value.save()
		return HttpResponse('Added')
	return render_to_response('specification_add.html', context={'product_id':id})

def about(request):
	return render_to_response('about.html')

# Custom filters


