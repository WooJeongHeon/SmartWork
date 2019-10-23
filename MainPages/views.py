from django.shortcuts import render, redirect
from AdminPages.models import UrlCostum
from MessageBoards.models import Category


def index(request):
	urlcostum = UrlCostum.objects.all()
	context = {'msgboards':urlcostum}
	context['category_list'] = Category.objects.all()

	return render(
		request,
		'main_site.html',
		context
	)


def about_me(request):
	urlcostum = UrlCostum.objects.all()
	context = {'msgboards':urlcostum}
	context['category_list'] = Category.objects.all()

	return render(
		request,
		'about_me.html',
		context
	)

def schedule(request):
	urlcostum = UrlCostum.objects.all()
	context = {'msgboards':urlcostum}
	context['category_list'] = Category.objects.all()

	return render(
		request,
		'schedule.html',
		context
	)



def robots(request):
    return render(
        request,
        'robots/robots.txt'
    )