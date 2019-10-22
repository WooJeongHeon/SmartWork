from django.shortcuts import render, redirect
from AdminPages.models import MsgBoards
from MessageBoards.models import Category


def index(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()

	return render(
		request,
		'main_site.html',
		context
	)


def about_me(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()

	return render(
		request,
		'about_me.html',
		context
	)



# def robots(request):
#     return render(
#         request,
#         'robots.txt'
#     )