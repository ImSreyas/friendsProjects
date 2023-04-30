from django.urls import path

from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
    path('viewusers', views.viewuser, name='viewusers'),
    path('edituser/<id>', views.edituser, name='edituser'),
    path('edituser1', views.edituser1, name='edituser1'),

    path('viewreview', views.viewreview, name='viewreview'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('viewalluser', views.viewalluser, name='viewalluser'),
    path('inactiveuser/<id>', views.inactiveuser, name='inactiveuser'),
    # path('adminhome', views.adminhome, name='adminhome'),
    path('logout', views.logout, name='logout'),
   ]
