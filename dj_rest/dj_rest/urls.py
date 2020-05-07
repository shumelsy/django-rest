"""dj_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/create/$', views.UserCreateView.as_view(), name="user_create"),
    url(r'^users/list/$', views.UsersListView.as_view(), name="users_list"),
    url(r'^users/(?P<pk>\d+)/detail/$', views.UserDetailView.as_view(), name="user_detail"),
    url(r'^users/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name="user_update"),
    url(r'^users/(?P<pk>\d+)/delete/$', views.UserDeleteView, name="user_delete"),  
]
