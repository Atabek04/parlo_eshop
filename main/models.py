from codecs import backslashreplace_errors
from xmlrpc.client import Boolean
from django.db import models

class Color(models.Model):
	title = models.CharField(max_length=50, blank=True)
	code = models.CharField(max_length=50, blank=True)
	level = models.IntegerField(blank=True, default=0)
	category = models.ForeignKey("Category", on_delete=models.CASCADE, null= True)

	def __str__(self):
		return self.title


class Size(models.Model):
	title = models.CharField(max_length=50, blank=True)
	code = models.CharField(max_length=50, blank=True)
	level = models.IntegerField(blank=True, default=0)
	category = models.ForeignKey("Category", on_delete=models.CASCADE, null= True)

	def __str__(self):
		return f" {self.title} - {self.code} "


class Tag(models.Model):
	title = models.CharField(max_length=50, blank = True)
	level = models.IntegerField(blank=True, default=0)

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=50, blank = True)
	parent = models.ForeignKey("Category", on_delete= models.CASCADE, blank= True, null= True)
	level = models.IntegerField(blank=True, default=0)
	good_count = models.IntegerField(default=0, blank = True)
	sub_category_count = models.IntegerField(default=0, blank= True)
	logo = models.ImageField(upload_to='uploads', blank = True)

	def __str__(self):
		result_title = self.title
		parent_model = self.parent
		while parent_model:
			result_title = parent_model.title + '=>' + result_title
			parent_model = parent_model.parent

		return result_title

class CategoryBrand(models.Model):
	title = models.CharField(max_length=50, blank = True)
	category = models.ForeignKey("Category", on_delete=models.CASCADE)
	level = models.IntegerField(blank=True, default=0)

	def __str__(self):
		return f"{self.category.title} - {self.title}"



class Good(models.Model):
	title = models.CharField(max_length=50, blank=True)
	category = models.ForeignKey("Category", on_delete=models.CASCADE)
	level = models.IntegerField(blank=True, default=0)
	old_price = models.FloatField(default=0)
	price = models.FloatField(default=0)
	rating = models.FloatField(default=0)
	short_description = models.TextField(max_length=200, blank=True)
	weight = models.TextField(max_length=200, blank=True)
	dimension = models.TextField(max_length=200, blank=True)
	materials = models.TextField(max_length=200, blank=True)
	extra = models.TextField(max_length=200, blank=True)
	description = models.TextField(max_length=400, blank=True)
	color = models.ForeignKey("Color", on_delete=models.CASCADE)
	size = models.ForeignKey("Size", on_delete=models.CASCADE)
	logo = models.ImageField(upload_to='uploads', blank=True)
	logo2 = models.ImageField(upload_to='uploads', blank=True)
	logo3 = models.ImageField(upload_to='uploads', blank=True)
	logo4 = models.ImageField(upload_to='uploads', blank=True)
	logo5 = models.ImageField(upload_to='uploads', blank=True)
	logo6 = models.ImageField(upload_to='uploads', blank=True)
	logo_vertical = models.ImageField(upload_to='uploads', blank=True)
	logo_horizontal = models.ImageField(upload_to='uploads', blank=True)
	is_main = models.BooleanField(default=False)
	is_new = models.BooleanField(default=False)
	is_popular = models.BooleanField(default=False)
	is_discount = models.BooleanField(default=False)
	brand = models.ForeignKey("CategoryBrand", on_delete=models.CASCADE,null=True, blank=True)
	stock = models.IntegerField(blank=True, default=0)


	def __str__(self):
		return f"{self.category}  ==>  {self.title}  ==> {self.color.title}  ==> {self.size	.title}"

	