from django.urls import path

from . import views

urlpatterns = [

    # path('index', views.index, name='index'),
    # path('register', views.register, name='register'),
    # path('login', views.login, name='login'),

    # path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
   ]
