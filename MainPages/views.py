from django.shortcuts import render, redirect
from AdminPages.models import MsgBoards


def index(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	return render(
		request,
		'main_site.html',
		context
	)


def about_me(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
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