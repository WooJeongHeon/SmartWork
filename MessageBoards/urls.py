"""my_site_prj URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('tag/<str:slug>/', views.PostListByTag.as_view()),
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('edit_comment/<int:pk>/', views.CommentUpdate.as_view()),

    # path('delete_comment/<int:pk>/', views.CommentDelete.as_view()), # CBV (Class Based View), views.py에서 CommentDelete class 사용.
    path('delete_comment/<int:pk>/', views.delete_comment),
    # FBV(Function Based View), views.py에서 delete_comment 함수 사용.

    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/update/', views.PostUpdate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),  # <int:pk>/: 정수값을 입력받고 입력받은 값을 pk라고 함
    path('create/', views.PostCreate.as_view()),
    path('', views.PostList.as_view()),  # 주소 뒤에 아무것도 안오면views.PostList로 가라
]
