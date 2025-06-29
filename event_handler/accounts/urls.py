from django.urls import path,include
from django.urls import re_path

from . import views


''' from here redirecting to individual app
as per the logged in is admin or user '''
urlpatterns = [
    path('login/',views.loginpage,name="login"),
    path('register/',views.registerpage,name="register"),
    path('',views.index,name="index"),
    path('logout/', views.logoutuser, name="logout"),
    path('user/', include('user.urls')),
   
    path('controller/', include('controller.urls')),
    path('forbidden/', views.forbidden, name="forbidden"),
]