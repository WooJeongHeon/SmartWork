from django.shortcuts import render
from ../AdminPages/models import MsgBoards


def msgboards(request):
	msgboards = MsgBoards.objects.all()
	context = {'msgboards':msgboards}
	return render(
        request,
        'navbar.html',
		context
    )
