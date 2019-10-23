from django.shortcuts import render, redirect
from AdminPages.models import UrlCostum
from MessageBoards.models import Category




def sign_in(request):
	urlcostum = UrlCostum.objects.all()
	context = {'msgboards':urlcostum}
	context['category_list'] = Category.objects.all()
	return render(
		request,
		'sign_in.html',
		context
	)

def sign_up(request):
	urlcostum = UrlCostum.objects.all()
	context = {'msgboards':urlcostum}
	context['category_list'] = Category.objects.all()	
	return render(
		request,
		'sign_up.html',
		context
	)

