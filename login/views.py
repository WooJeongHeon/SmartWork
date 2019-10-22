from django.shortcuts import render, redirect
from AdminPages.models import MsgBoards
from MessageBoards.models import Category




def sign_in(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()
	return render(
		request,
		'sign_in.html',
		context
	)

def sign_up(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()	
	return render(
		request,
		'sign_up.html',
		context
	)

