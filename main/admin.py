from django.contrib import admin
from .models import Category, Product, SpecificationField, SpecificationInstance, SpecificationInstanceValue, News
from django import forms

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ('date_created','title','text',)

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

class SpecificationInstanceValueInline(admin.TabularInline):
	model = SpecificationInstanceValue
	fields = ['specification_field', 'specification_instance','value']
	extra = 1

#	def __init__(self, *args, **kwargs):
#		self.parent_object = kwargs['obj']
#		del kwargs['obj']
#		super (ExchangeInline, self).__init__(*args, **kwargs)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		instance = self.get_object(request, SpecificationInstance)
		kwargs['queryset']=SpecificationField.objects.filter(product__pk=instance.product.pk)
		return super(SpecificationInstanceValueInline, self).formfield_for_foreignkey(db_field, **kwargs)

	def get_object(self, request, model):
		object_id = request.META['PATH_INFO'].strip('/').split('/')[-2]
		return model.objects.get(pk=int(object_id))

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'category', 'desctiption', 'admin_thumbnail','promoted')
	inlines = [SpecificationFieldInline, SpecificationInstanceInline]
	search_fields = ['id']


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
