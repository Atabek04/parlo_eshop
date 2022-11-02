from django.db import models
from requests import session
from datetime import datetime

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


class Cart(models.Model):
	title = models.CharField(max_length = 200, blank = True)
	email = models.CharField(max_length = 200, blank = True)
	last_name = models.CharField(max_length = 200, blank = True)
	first_name = models.CharField(max_length = 200, blank = True)
	zip_code = models.CharField(max_length = 200, blank=True)
	country = models.CharField(max_length = 200, blank = True)
	city = models.CharField(max_length = 200, blank = True)
	person = models.CharField(max_length = 200, blank = True)
	phone = models.CharField(max_length = 200, blank = True)
	address = models.CharField(max_length = 200, blank = True)
	title = models.CharField(max_length = 200, blank = True)

	is_accepted = models.BooleanField(default = False)
	is_payed = models.BooleanField(default = False)
	status = models.IntegerField(default = 0)

	session_id = models.CharField(max_length = 200, blank = True)
	amount = models.IntegerField(default=1)
	discount = models.IntegerField(default=0)
	orig_price = models.FloatField(default=0)
	price = models.FloatField(default=0)
	crated_at = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return f'{self.session_id}+ {self.title}'


class CartItem(models.Model):
	good = models.ForeignKey(Good, on_delete = models.CASCADE)
	cart = models.ForeignKey('Cart', on_delete = models.CASCADE)
	amount = models.FloatField(default = 0)
	price = models.FloatField(default=0)
	status = models.IntegerField(default = 0) # 0 - created, -1 deleted
	all_price = models.FloatField(default = 0)

	def __str__(self):
		return f'{self.cart.id} - {self.good.title} - {self.amount}'


class CompareItem(models.Model):
	good = models.ForeignKey(Good, on_delete = models.CASCADE)
	session_id = models.CharField(max_length = 200, blank = True)
	status = models.IntegerField(default = 0)

	def __str__(self):
		return f'{self.session_id} {self.good.title}' 

class WishItem(models.Model):
	good = models.ForeignKey(Good, on_delete=models.CASCADE)
	session_id = models.CharField(max_length = 200, blank = True)
	status = models.IntegerField(default = 0)

	def __str__(self):
		return f'{self.session_id} {self.good.title}' 


class Subscriber(models.Model):
	email = models.CharField(max_length=200)
	status = models.IntegerField(default = 0)

	def __str__(self):
		return self.email