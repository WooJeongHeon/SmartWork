from django.shortcuts import render
from .models import UrlCostum
from MessageBoards.models import Category
from vacation.models import Vacation
from django.views.generic import ListView



def admin_tools(request):
	urlcostum = UrlCostum.objects.all()
	context = {'msgboards':urlcostum}
	context['category_list'] = Category.objects.all()
	context['vacation_list'] = Vacation.objects.all()


	return render(
        request,
        'admin_tools.html',
	    context
    )

def headcount(request):
    urlcostum = UrlCostum.objects.all()
    context = {'msgboards':urlcostum}
    context['category_list'] = Category.objects.all()
    context['vacation_list'] = Vacation.objects.all()


    return render(
        request,
        'headcount.html',
	    context
    )

def custom_site(request):
    urlcostum = UrlCostum.objects.all()
    context = {'msgboards':urlcostum}
    context['category_list'] = Category.objects.all()
    context['vacation_list'] = Vacation.objects.all()
    
    return render(
        request,
        'custom_site.html',
	    context
    )