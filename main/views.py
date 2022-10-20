from math import ceil
from tracemalloc import start
from unicodedata import category
from django.shortcuts import render
from main.models import *


def indexHandler(request):
	categories = Category.objects.all()

	context = {
		'categories': categories,
	}
	return render(request, 'index-3.html', context)


def catalogHandler(request):
	categories = Category.objects.all()

	context = {
		'categories': categories,
	}
	return render(request, 'catalog.html', context)


def catalogItemHandler(request, catalog_id):
	active_category = Category.objects.get(id=catalog_id)
	categories = Category.objects.all()
	brands = CategoryBrand.objects.filter(category__id=catalog_id)
	colors = Color.objects.filter(category__id=catalog_id)
	sizes = Size.objects.filter(category__id=catalog_id)
	tags = Tag.objects.all()
	goods = Good.objects.filter(category__id=catalog_id)

	search_value = request.GET.get('q', None)

	active_brands = request.GET.getlist('active_brand', [])
	active_brands = [int(i) for i in active_brands]

	active_colors = request.GET.getlist('active_color', [])
	active_colors = [int(i) for i in active_colors]

	active_sizes = request.GET.getlist('active_size', [])
	active_sizes = [int(i) for i in active_sizes]

	is_discount  = request.GET.get('is_discount', None)
	is_new  = request.GET.get('is_new', None)
	stock  = request.GET.get('stock', None)
	

	price = request.GET.get('price', None)
	price_start, price_stop = None,None
	if price and len(price.split('-'))==2:
		price_start = int(price.split('-')[0])
		price_stop = int(price.split('-')[1])

	if search_value:
		new_goods = []
		for g in goods:
			if g.title.finds(search_value):
				new_goods.append(g)
		goods = new_goods

	if active_brands:
		new_goods = []
		for g in goods:
			if g.brand and g.brand.id in active_brands:
				new_goods.append(g)

		goods = new_goods

	if active_colors:
		new_goods = []
		for g in goods:
			if g.color and g.color.id in active_colors:
				new_goods.append(g)

		goods = new_goods

	if active_sizes:
		new_goods = []
		for g in goods:
			if g.size.id in active_sizes:
				new_goods.append(g)

		goods = new_goods

	if is_discount:
		new_goods = []
		for g in goods:
			if g.is_discount:
				new_goods.append(g)

		goods = new_goods
	
	if is_new:
		new_goods = []
		for g in goods:
			if g.is_new:
				new_goods.append(g)

		goods = new_goods

	if stock:
		new_goods = []
		for g in goods:
			if g.stock > 0 :
				new_goods.append(g)

		goods = new_goods

	if price_start != None and price_stop:
		new_goods = []
		for g in goods:
			if g.price >= price_start and g.price <=price_stop:
				new_goods.append(g)

		goods = new_goods


	limit = int(request.GET.get('limit', 3))
	current_page = int(request.GET.get('page', 1))
	total =  len(goods)
	pages_count = ceil (total/limit)
	pages = range(1, pages_count+1)

	stop = current_page*limit
	start = stop - limit
	prev_page = current_page - 1
	next_page = current_page + 1

	context = {
		'categories': categories,
		'goods': goods[start:stop],
		'brands': brands,
		'sizes': sizes,
		'colors': colors,
		'tags': tags,
		'active_category': active_category,
		'search_value': search_value,
		'active_brands':active_brands,
		'active_colors':active_colors,
		'active_sizes':active_sizes,
		'stock':stock,
		'is_discount':is_discount,
		'is_new':is_new,
		'pages': pages,
		'current_page':current_page,
		'pages_count':pages_count,
		'prev_page':prev_page,
		'next_page':next_page,
		'start':start,
		'stop':stop,
		'total':total,
		
	}
	return render(request, 'catalog.html', context)


def goodHandler(request, good_id):
	active_good = Good.objects.get(id=good_id)
	categories = Category.objects.all()
	related_products = Good.objects.filter(category__id = active_good.category.id).exclude(id = good_id)[:4]

	context = {
		'active_good':active_good,
		'categories':categories,
		'related_products':related_products,

	}
	return render(request, 'product-details.html', context)


