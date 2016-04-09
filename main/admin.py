from django.contrib import admin
from .models import Category, Product, SpecificationField, SpecificationInstance, SpecificationInstanceValue

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
	extra = 1

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
