from django.shortcuts import render, redirect
from django.contrib import messages
from pred_app.lstm_prediction import *
from django.contrib.auth.models import User,auth
from . models import review
from django.template import loader
from django.http import HttpResponse
from datetime import date
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout




# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')

def index(request):
	return render(request, 'pred_app/index.html') 

def register(request):
	if request.method=="POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username already taken")
				return redirect('/pred_app/register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email already taken")
			else:
				user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
				# user=User()
				# user.first_name=first_name
				# user.last_name=last_name
				# user.email=email
				# user.username=username
				# user.password=password1
				user.save()
				print("User Created")
		else:
			print("Password Not Match")
			return redirect('/pred_app/register')
		return redirect('/pred_app/login')
	else:
		return render(request, 'pred_app/register.html')

def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		if User.objects.filter(username=username,password=password):
				data=User.objects.get(username=username,password=password)
				if data.username=="admin":
					template = loader.get_template('pred_app/adminhome.html')
					context = {}
					return HttpResponse(template.render(context,request))
				else:
					data=User.objects.get(username=username)
					if data.is_active==False:
						messages.info(request,"User is inactive")
					else:
						request.session["username"]=username
						return redirect('/pred_app/pred')
		else:
			return redirect('/pred_app/login')
		# user=auth.authenticate(username=username,password=password)
		# if user is not None:
		# 	auth.login(request,user)
		# 	request.session["username"]=username
		# 	return redirect('/pred_app/pred')
		# else:
		# 	messages.info(request,"Invalid Details")
		# 	return redirect('/pred_app/login')
	return render(request,'pred_app/login.html')

def logout(request):
	try:
		del request.session['username']
	except:
		pass
	# auth.logout(request)
	return render(request,'pred_app/index.html')

# def logout(request):
# 	auth.logout(request)
# 	return redirect('/')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def logout(request):
# 	del request.session["username"]
# 	return redirect('/')


def pred(request):
    return render(request, 'pred_app/prediction.html')

def contact(request):
	username=request.session['username']
	if request.method=="POST":
		title=request.POST['title']
		feedback=request.POST['content']
		re=review()
		re.title=title
		re.feedback=feedback
		re.username=username
		re.feeddate=date.today()
		re.save()
	return render(request, 'pred_app/contact.html')

def search(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})
# -----------------------------------------------------------

def viewuser(request):
	username=request.session['username']
	data = User.objects.get(username=username)
	template = loader.get_template('pred_app/viewusers.html')
	context = {'data':data}
	return HttpResponse(template.render(context,request))

def inactiveuser(request,id):
	user=User.objects.get(id=id)
	if user.is_active==True:
		user.is_active=False
		user.save()
	else:
		user.is_active=True
		user.save()
	return HttpResponse("<script> alert('Status Updated');window.location='/pred_app/viewalluser';</script>")

	# data = User.objects.all()
	# template = loader.get_template('pred_app/viewalluser.html')
	# context = {'data':data}
	# return HttpResponse(template.render(context,request))

	

def viewalluser(request):
	data = User.objects.all()
	template = loader.get_template('pred_app/viewalluser.html')
	context = {'data':data}
	return HttpResponse(template.render(context,request))

def viewreview(request):
	data = review.objects.all()
	template = loader.get_template('pred_app/viewreview.html')
	context = {'data':data}
	return HttpResponse(template.render(context,request))

def forgetpassword(request):
	if request.method=="POST":
		username=request.POST['username']
		data=User.objects.get(username=username)
		if data:
			password=request.POST['new_password']
			cpassword=request.POST['con_password']
			if password==cpassword:
				data.password=password
				data.save()
			else:
				return HttpResponse("<script> alert('Password Mismatch');window.location='/pred_app/forgetpassword';</script>")

	return render(request,'pred_app/passwordchange.html')

def edituser(request,id):
		data=User.objects.get(id=id)
		request.session['id']=id
		template = loader.get_template('pred_app/edituser.html')
		context = {'data':data}
		return HttpResponse(template.render(context,request))

def edituser1(request):
	id=request.session['id']
	first_name=request.POST['first_name']
	last_name=request.POST['last_name']
	email=request.POST['email']
	data=User.objects.get(id=id)
	data.first_name=first_name
	data.last_name=last_name
	data.email=email
	data.save()
	data=User.objects.get(id=id)
	template = loader.get_template('pred_app/viewusers.html')
	context = {'data':data}
	return HttpResponse(template.render(context,request))
	
	

def changepassword(request):
	username=request.session['username']
	if request.method=="POST":
		old_password=request.POST['old_password']
		if User.objects.filter(username=username,password=old_password):
			new_password=request.POST['new_password']
			confirm_password=request.POST['confirm_password']
			if new_password==confirm_password:
				data=User.objects.get(username=username)
				data.password=new_password
				data.save()
			else:
				return HttpResponse("<script> alert('Password Mismatch');window.location='/pred_app/changepassword';</script>")
		else:
			return HttpResponse("<script> alert('Password Incorrect');window.location='/pred_app/changepassword';</script>")
	return render(request,'pred_app/changepassword.html')

# def adminhome(request):
#     return render(request, 'pred_app/adminhome.html')
