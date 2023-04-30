from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', views.adlogin, name="adlogin"),
    path('hotel/', views.htreg, name="htreg"),
    path('hotel/login', views.hotlogin, name="hotlogin"),
    path('hotel/home', views.hthome, name="hthome"),
    path('hotel/update', views.htprofile, name="htprofile"),
    path('hotel/additem', views.additems, name="additems"),
    ]