from Home import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path("feature",views.feature,name='feature'),
    path("myprofile",views.myprofile,name='myprofile'),
    path("myorders",views.myorders,name='myorders'),
    path("logout",views.logoutuser,name='logout'),
    path("login1",views.login,name='login'),
    path("signup",views.signup,name='signup')
]
