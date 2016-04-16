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

def check_bottom_cell_rowspan(field, this_value, index, instances_list, depth=0):
	
	if index == len(instances_list)-1:
		return depth
	
	that_value = find_value(field, instances_list[index])
	if that_value==this_value:
		depth += 1
		return check_bottom_cell_rowspan(field, this_value, index+1, instances_list, depth)
	else:
		return depth


@register.filter
def specification_cell_filter(field, row):
	flag = False
	product = row.product
	
	instances_list = list(product.specificationinstance_set.all())
	index = instances_list.index(row)
	#Counter of colspan
	counter_rowspan = 0;
	this_value = find_value(field, row)

	counter_rowspan = check_bottom_cell_rowspan (field, this_value, index, instances_list, 0)
#	for r in range(index, len(instances_list)):
#		that_value=find_value(field, instances_list[r])
#		if that_value==this_value:
#			counter_rowspan += 1

	if (index != 0) and (find_value(field, instances_list[index-1]) == this_value):
		return None
	else:
		return "<td rowspan="+ str(counter_rowspan) +">"+ this_value +"</td>"
	

