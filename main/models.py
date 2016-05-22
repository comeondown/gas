from django.db import models
from django.core.files.storage import FileSystemStorage
from redactor.fields import RedactorField



class Category(models.Model):
	title = models.CharField(max_length=300, unique=True)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return '{}'.format(self.title)

class Product(models.Model):
	title = models.CharField(max_length=300, verbose_name="Название")
	category = models.ForeignKey(Category)
	desctiption = RedactorField(max_length=3000, verbose_name="Описание")
	text = RedactorField(max_length=3000, verbose_name="Особенности", blank=True)
	image = models.ImageField(upload_to='images/')
	specification_image = models.ImageField(upload_to='images/specifications')
	promoted = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

	def __str__(self):
		return '{}'.format(self.title)

	def admin_thumbnail(self):
		return u'<img src="{0}" height="300px"/>'.format(self.image.url)

	admin_thumbnail.short_description = 'Thumbnail'
	admin_thumbnail.allow_tags = True

#type of column in specification table
class SpecificationField(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=400)
	measure = models.CharField(max_length=50, blank=True)

	class Meta:
		verbose_name = 'Поле спецификации'
		verbose_name_plural = 'Поля спецификации'

	def __str__(self):
		return '{}'.format(self.title)

#specification row
class SpecificationInstance(models.Model):
	product = models.ForeignKey(Product)
	index = models.CharField(max_length=100)
	number= models.IntegerField()

	class Meta:
		verbose_name = 'Экземпляр спецификации'
		verbose_name_plural = 'Экземпляры спецификации'
		ordering = ['number']

	def __str__(self):
		return '{}'.format(self.index)

	def selflink(self):
		if self.id:
			return "<a href='/admin/main/specificationinstance/{}' target='_blank'>Edit</a>".format(self.id)
		else:
			return "Not present"

	selflink.allow_tags = True

#value that write in cell
class SpecificationInstanceValue(models.Model):
	specification_instance = models.ForeignKey(SpecificationInstance)
	specification_field = models.ForeignKey(SpecificationField)
	value = models.CharField(max_length=1500)


	class Meta:
		verbose_name = 'Значение поля спецификации'
		verbose_name_plural = 'Значения полей спецификации'
#Table of texts
class Texts(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	text = RedactorField(max_length=3000, verbose_name='Текст')

class News(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=500, verbose_name='Название новости')
	text = RedactorField(max_length=3000, verbose_name='Текст новости')
