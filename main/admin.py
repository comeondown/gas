from django.contrib import admin
from .models import Category, Product, SpecificationField, SpecificationInstance, SpecificationInstanceValue
from django import forms

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title',)

class SpecificationFieldInline(admin.TabularInline):
	model = SpecificationField
	extra = 1

class SpecificationInstanceInline(admin.StackedInline):
	readonly_fields = ['selflink',]
	model = SpecificationInstance
	extra = 1

#class SpecificationInstanceValueInlineForm(forms.ModelForm):

#	def __init__(self, *args, **kwargs):
#		super(SpecificationInstanceValueInlineForm, self).__init__(*args, **kwargs)
#		self.fields['specification_field'].queryset = SpecificationField.objects.filter(product__exact=self.instance.specification_instance)


class SpecificationInstanceValueInline(admin.TabularInline):

	model = SpecificationInstanceValue
	fields = ['specification_field', 'specification_instance']
	extra = 1
#	form = SpecificationInstanceValueInlineForm





	def formfield_for_foreignkey(self, db_field, request=None, obj=None, **kwargs):
	
		field = super(SpecificationInstanceValueInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
		instance = SpecificationInstance.objects.get(id=request.GET['instance'])
		field.queryset = field.queryset.filter(product__exact = instance.product)
		
		return field

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'desctiption', 'admin_thumbnail',)
	inlines = [SpecificationFieldInline, SpecificationInstanceInline]



@admin.register(SpecificationField)
class SpecificationFieldAdmin(admin.ModelAdmin):
	list_display = ('product', 'title', 'measure')


@admin.register(SpecificationInstance)
class SpecificationInstanceAdmin(admin.ModelAdmin):
	list_display = ('index', 'product')
	inlines = [SpecificationInstanceValueInline]
	search_fields = ['index']

@admin.register(SpecificationInstanceValue)
class SpecificationInstanceValueAdmin(admin.ModelAdmin):
	list_display = ('specification_instance', 'specification_field', 'value')





# Register your models here.
