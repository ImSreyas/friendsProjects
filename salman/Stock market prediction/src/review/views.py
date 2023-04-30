from django.shortcuts import render
from django.contrib import messages
from pred_app.lstm_prediction import *
from . models import review
from django.template import loader

# Create your views here.
def logout(request):
	auth.logout(request)
	return redirect('/')

def pred(request):
    return render(request, 'pred_app/prediction.html')

def contact(request):
	if request.method=="POST":
		title=request.POST['title']
		content=request.POST['content']
		review=review.objects.create(title=title,content=content)
		review.save()
	return render(request, 'pred_app/contact.html')

