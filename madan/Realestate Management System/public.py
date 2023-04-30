from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def index():
	return render_template('index.html')


@public.route('/register',methods=['get','post'])
def register():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['gender']
		address=request.form['address']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		pincode=request.form['pincode']
		uname=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'" %(uname,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
		else:
			q="insert into login values(null,'%s','%s','customer')"%(uname,password)
			res=insert(q)
			q="insert into customer values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,gender,address,place,phone,email,pincode)
			insert(q)
			flash("Registered successfully")
	return render_template('userregister.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pas=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(uname,pas)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']	
			if res[0]['usertype']=="customer":
				flash("Login Successfully")
				return redirect(url_for('user.userhome'))
			if res[0]['usertype']=="admin":
				flash("Login Successfully")
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="seller":
				flash("Login Successfully")
				return redirect(url_for('seller.sellerhome'))
		else:
			flash("invalid username and password")
	return render_template("login.html")


@public.route('/sellerregister',methods=['get','post'])
def sellerregister():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['gender']
		address=request.form['address']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		pincode=request.form['pincode']
		uname=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'" %(uname,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
		else:
			q="insert into login values(null,'%s','%s','seller')"%(uname,password)
			res=insert(q)
			q="insert into seller values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,gender,address,phone,email,place,pincode)
			insert(q)
			flash("Registered successfully")
	return render_template('sellerregister.html')

