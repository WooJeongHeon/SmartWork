from django.shortcuts import render

def index(request):
    return render(
        request,
        'admin_index.html'
    )

def msgboards(request):
    return render(
        request,
        'msgboards.html'
    )