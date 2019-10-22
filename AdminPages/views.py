from django.shortcuts import render
from .models import MsgBoards
from MessageBoards.models import Category
from django.views.generic import ListView



def admin_tools(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()

	return render(
        request,
        'admin_tools.html',
	    context
    )

def headcount(request):
    msgboards = MsgBoards.objects.all()
    context = {'msgboards':msgboards}
    context['category_list'] = Category.objects.all()

    return render(
        request,
        'headcount.html',
	    context
    )

def custom_site(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()

	return render(
        request,
        'custom_site.html',
	    context
    )