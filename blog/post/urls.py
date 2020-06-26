"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from .views import blogListView, blogDetailView , blogUpdateView, blogDeleteView
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register , name='register'),
    path('home/',blogListView.as_view(),name='home'),
    path('blog/<int:pk>/delete',blogDeleteView.as_view(),name='blog-delete'),
    path('blog/<int:pk>/update',blogUpdateView.as_view(),name='blog-update'),
    path('blog/<int:pk>/',blogDetailView.as_view(),name='blog-detail'),
    path('login/',views.login,name='login'),
    path('logout/' , views.logouts , name='logouts'),
    path('posts/' , views.posts , name='posts'),
    
]
