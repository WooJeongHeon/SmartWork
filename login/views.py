from django.shortcuts import render, redirect
from AdminPages.models import MsgBoards



def sign_in(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	return render(
		request,
		'sign_in.html',
		context
	)

def sign_up(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	return render(
		request,
		'sign_up.html',
		context
	)


# =============================================== 밑에는 네이버 참고 복붙

from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form})  

