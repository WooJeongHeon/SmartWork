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

    path('create/', views.VacationCreate.as_view()),
    path('', views.VacationList.as_view()), # 주소 뒤에 아무것도 안오면views.PostList로 가라
    path('<int:pk>/', views.VacationDetail.as_view()),
	path('<int:pk>/update/', views.VacationUpdate.as_view()),


]