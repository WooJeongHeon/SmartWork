from django.shortcuts import render, redirect


# def index(request):
#     # return redirect('/blog/') # https://programtest11.run.goorm.io/blog/ 로 리다이렉트
#     return render(
#         request,
#         'wjh_main_site.html'
#     )


def about_me(request):
    return render(
        request,
        'about_me.html'
    )

# def robots(request):
#     return render(
#         request,
#         'robots.txt'
#     )