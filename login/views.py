from django.shortcuts import render, redirect


def sign_in(request):
    return render(
        request,
        'sign_in.html'
    )
