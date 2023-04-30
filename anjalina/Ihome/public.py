from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def pubhome():
	return render_template("index.html")

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pas=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(uname,pas)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="provider":
				return redirect(url_for("provider.providerhome"))
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="user":
				return redirect(url_for('user.userhome'))
		else:
			flash("invalid username and password")
	return render_template("login.html")
@public.route('/providerreg',methods=['get','post'])
def providerreg():
	data={}
	if 'submit' in request.form:
		ar=request.form['ar']
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		pincode=request.form['pin']
		phn=request.form['phn']
		email=request.form['email']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="select * from login where username='%s' and password='%s'" %(uname,pwd)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
		else:
			q="insert into login values(null,'%s','%s','provider')"%(uname,pwd)
			res=insert(q)
			q="insert into service_provider values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,ar,fname,lname,place,pincode,phn,email)		
			insert(q)
			flash("Registered successfully")
			return redirect(url_for('public.login'))
	q="select * from area"
	res=select(q)
	data['selarea']=res
	return render_template("service_provider_registration.html",data=data)


@public.route('/userreg',methods=['get','post'])
def userreg():
	data={}
	if 'submit' in request.form:
		ar=request.form['area']
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pincode=request.form['pincode']
		dis=request.form['dis']
		contact=request.form['contact']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['pwd']
		q="select * from login where username='%s' and password='%s'" %(uname,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
		else:
			q="insert into login values(null,'%s','%s','user')"%(uname,password)
			res=insert(q)
			q="insert into users values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,ar,fname,lname,hname,place,pincode,dis,contact,email)
			insert(q)
			flash("Registered successfully")
			return redirect(url_for('public.login'))
	q="select * from area"
	res=select(q)
	data['ar']=res
	return render_template('userregister.html',data=data)


@public.route('/reset_password',methods=['get','post'])
def reset_password():
	# ids=session['login_id']
	if 'submit' in request.form:
		pwd=request.form['pwd']
		q="update login set password='%s' where  usertype='user'" %(pwd)
		update(q)
		flash("Password Reset")
		return redirect(url_for('public.login'))
	return render_template('reset_password.html')