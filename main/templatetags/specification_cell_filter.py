from django import template
from main.models import *

register = template.Library()

"""
@register.filter
def specification_cell_filter(cell, field):
	if cell.specification_field == field:
		return "<td>"+str(cell.value)+"</td>"
	else:
		return "<td></td>"
"""
def find_value(field ,row):
	for v in row.specificationinstancevalue_set.all():
		if v.specification_field == field:
			return v.value
	return ''

@register.filter
def specification_cell_filter(field, row):
	flag = False
	product = row.product
	
	instances_list = list(product.specificationinstance_set.all())
	index = instances_list.index(row)
	#Counter of colspan
	counter_colspan = 0;
	this_value = find_value(field, row)

	for r in range(index, len(instances_list)):
		that_value=find_value(field, instances_list[r])
		if that_value==this_value:
			counter_colspan += 1

	if (index != 0) and (find_value(field, instances_list[index-1]) == this_value):
		return None
	else:
		return "<td rowspan="+ str(counter_colspan) +">"+ this_value +"</td>"
	

