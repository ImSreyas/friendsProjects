from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .models import User
from .dbset import upatehotelinf
from .forms import RegistrationForm
from django.contrib import messages

import datetime
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
        form= RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            return redirect('hotlogin')
        else:
            messages.error(request, form.errors)
      else:
            form= RegistrationForm()    
      return render(request,'hotel/index.html', {'form' : form})

def hotlogin(request):
     context=''
     if request.method=="POST":
       
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user:
            if user is not None and user.is_fudhotel:
                login(request, user)
                current_user = request.user
                request.session['hotids']= current_user.id
                return redirect('hthome')
            else:
                context = {'error': 'Wrong credintials'}  # to display error?
              
     return render(request,'hotel/login.html', {'context': context})


def hthome(request):
      return render(request,'hotel/home.html')


def additems(request):
      return render(request,'hotel/additem.html')

def htprofile(request):
    if request.method == 'POST':
        if upatehotelinf(request):
            messages.success(request, "info Updated.")
        else:
            messages.success(request, "Something error.")
            
    return render(request,'hotel/updatepro.html')