from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .models import User,categorys,items,HotProfile,categorys,tempcart,orders,userregs
from .dbset import upatehotelinf,hotelereg,additemsdb,addtempcart,addorder,usrreg
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic.base import ContextMixin
import datetime
from django.views.generic import TemplateView,ListView
from django.core.files.storage import FileSystemStorage
import sys
sys.setrecursionlimit(2000)
from django.utils.crypto import get_random_string
from django import template
register = template.Library()


@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return qty * unit_price

class YourView(ListView):
    template_name = 'books/acme_list.html'
    context_object_name = 'object_list'
    queryset = categorys.objects.all()

def userhome(request):
    carttmps=get_random_string(length=15)
    itms=items.objects.values()
    if 'cartids' not in request.session:
            request.session['cartids']=carttmps
    else:
            carttmps = request.session.get('cartids')

    return render(request,'user/index.html',{'z': itms.all()})


def paymets(request):
    amts=request.session.get('ttamt')
    return render(request,'payment/index.html',{'amts': amts})

def useritems(request,value):
     #bkid= request.GET.get('value', None)
     cats=categorys.objects.filter(id=value)
     ids=value
     itms=items.objects.filter(catsgry=value)
     if request.method == 'POST':
            if addtempcart(request)==1:
               return redirect('useritems', value=ids)
            else:
                messages.error(request, "Something error.")

     return render(request,'user/itemlist.html',{'z': itms.all()})

def viewcart(request):
      catstps=tempcart.objects.filter(cattempid=request.session.get('cartids'))
      if request.method == 'POST':
            totalamt=request.POST.get('ttlamt')
            request.session['ttamt']= totalamt
            if addorder(request)==1:
               return redirect('paymets')
            else:
                messages.error(request, "Something error.")
      return render(request,'user/cartview.html',{'catitems': catstps.all()})

def userlogin(request):
      context=''
      if request.method=="POST":
            username=request.POST.get('Username')
            password=request.POST.get('Password')
            sellers=userregs.objects.filter(useremail=username, userpass=password ).values()
            if sellers.count() == 1:
                
                    current_user = sellers.get()['id']
                    request.session['fduser']= current_user
                    request.session['fdusrnam']= sellers.get()['username']
                    return redirect('userhome')
            else:
                context ='Wrong credintials'
      return render(request,'user/logins.html')

def userregister(request):
     if request.method == 'POST':
        if usrreg(request):
            return redirect('userlogin')
        else:
            messages.error(request, "Something error.")
        
     return render(request,'user/register.html')

def adlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user:
            if user is not None and user.is_panuser:
                login(request, user)
                return redirect('uhome')
            elif user is not None and user.is_panofficer:
                login(request, user)
                return redirect('ofhome')  
            elif user is not None and user.is_panadmin:
                login(request, user)
                return redirect('adhome')    
    return render(request,'admins/index.html')

def htreg(request):
      if request.method == 'POST':
        if hotelereg(request):
            return redirect('hotlogin')
        else:
            messages.error(request, "Something error.")
      return render(request,'hotel/index.html')

def hotlogin(request):
        context=''
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            sellers=HotProfile.objects.filter(email=username, password=password ).values()
        if sellers.count() == 1:
               
                current_user = sellers.get()['id']
                request.session['hotuser']= current_user
                request.session['hotusrnam']= sellers.get()['hname']
                return redirect('hthome')
        else:
                context ='Wrong credintials'
              
        return render(request,'hotel/login.html', {'context': context})


def hthome(request):
      return render(request,'hotel/home.html')

def htprofile(request):
    if request.method == 'POST':
        if upatehotelinf(request):
            messages.success(request, "info Updated.")
        else:
            messages.success(request, "Something error.")
            
    return render(request,'hotel/updatepro.html')

def additems(request):
      cats=categorys.objects.values()
      if request.method == 'POST':
        if additemsdb(request)==1:
              messages.success(request, "Item added")
        else:
              messages.error(request, "Something error.")
      return render(request,'hotel/additem.html',{'catgris': cats.all()})

