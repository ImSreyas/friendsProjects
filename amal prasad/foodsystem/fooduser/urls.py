from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [


    path('', views.userhome, name="userhome"),
    path('items/<int:value>', views.useritems, name="useritems"),
    path('login', views.userlogin, name="userlogin"),
    path('register', views.userregister, name="userregister"),
    path('cartv', views.viewcart, name="viewcart"),
    path('payment', views.paymets, name="paymets"),
    path('admin/', admin.site.urls),
    path('admins/', views.adlogin, name="adlogin"),
    

    path('hotel/', views.htreg, name="htreg"),
    path('hotel/login', views.hotlogin, name="hotlogin"),
    path('hotel/home', views.hthome, name="hthome"),
    path('hotel/update', views.htprofile, name="htprofile"),
    path('hotel/additem', views.additems, name="additems"),
    ]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)