from flask import *
from database import *
import speech_recognition as sr

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from utils import extract_feature,convert
import pickle
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

user=Blueprint('user',__name__)

@user.route('/userhome',methods=['get','post'])
def userhome():
	return render_template('userhome.html')

@user.route('/send_feedback',methods=['get','post'])
def send_feedback():
	ids=session['login_id']
	if 'submit' in request.form:
		feedback=request.form['feedback']
		q="insert into feedback values(null,(select user_id from user where login_id='%s'),'%s','pending',Curdate())"%(ids,feedback)
		insert(q)
		flash("Feedback Sended")
	return render_template('usersend_feedback.html')

@user.route('/view_feedback',methods=['get','post'])
def view_feedback():
	data={}
	ids=session['login_id']
	q="select *,concat(fname,' ',lname)as NAME from feedback inner join user using(user_id) where login_id='%s'"%(ids)
	res=select(q)
	data['feed']=res
	return render_template('userview_feedback.html',data=data)

@user.route('/my_profile',methods=['get','post'])
def my_profile():
	data={}
	ids=session['login_id']
	q="select *,concat(fname,' ',lname)as NAME from user where login_id='%s'"%(ids)
	res=select(q)
	data['us']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		q="delete from user where user_id='%s'"%(id)
		delete(q)
		flash("Account Deleted")
		return redirect(url_for('user.userhome'))
	if action=="update":
		q="select * from user where login_id='%s'"%(ids)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		address=request.form['address']
		phone=request.form['phone']
		email=request.form['email']
		q="update user set fname='%s',lname='%s',address='%s',phone='%s',email='%s' where user_id='%s'"%(fname,lname,address,phone,email,id)
		update(q)
		flash("Profile Updated")
		return redirect(url_for('user.my_profile'))
	return render_template('userview_myprofile.html',data=data)

@user.route('/speech_text',methods=['get','post'])
def speech_text():
	transcript = ""
	if request.method == "POST":
		print("FORM DATA RECEIVED")
		if "file" not in request.files:
			return redirect(request.url)
		file = request.files["file"]
		if file.filename == "":
			return redirect(request.url)
		if file:
			recognizer = sr.Recognizer()
			audioFile = sr.AudioFile(file)
			with audioFile as source:
				data = recognizer.record(source)
			transcript = recognizer.recognize_google(data, key=None)
	return render_template('userspeech_text.html',transcript=transcript)

@user.route('/results',methods=['get','post'])
def results():
	if not os.path.isdir("./audio"):
		os.mkdir("audio")
	if request.method == 'POST':
		try:
			f = request.files['file']
			filename = secure_filename(f.filename)
			f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
		except:
			return render_template('userspeech_emotiontext.html', value="")

	wav_file_pre  = os.listdir("./audio")[0]
	wav_file_pre = f"{os.getcwd()}/audio/{wav_file_pre}"
	wav_file = convert(wav_file_pre)
	os.remove(wav_file_pre)
	model = pickle.load(open(f"{os.getcwd()}/model.model", "rb"))
	x_test =extract_feature(wav_file)
	y_pred=model.predict(np.array([x_test]))
	os.remove(wav_file)
	return render_template('userspeech_emotiontext.html', value=y_pred[0])
	print(y_pred)
	return render_template('userspeech_emotiontext.html')