from django.shortcuts import render, redirect


def index(request):
    return render(
        request,
        'main_site.html'
    )


def about_me(request):
    return render(
        request,
        'about_me.html'
    )

def test(request):
    return render(
        request,
        'test.html'
    )

def test2(request):
    return render(
        request,
        'test2.html'
    )

# def robots(request):
#     return render(
#         request,
#         'robots.txt'
#     )