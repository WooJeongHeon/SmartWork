from django.shortcuts import render
from .models import MsgBoards
from MessageBoards.models import Category
from django.views.generic import ListView

def index(request):
    msgboards = MsgBoards.objects.all()
    context = {'msgboards':msgboards}
    context['category_list'] = Category.objects.all()

    return render(
        request,
        'admin_index.html',
	    context
    )

def msgboards(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	context['category_list'] = Category.objects.all()

	return render(
        request,
        'msgboards.html',
	    context
    )