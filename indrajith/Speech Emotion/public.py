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
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if len(res)>0:
			flash("Already Exists")
		else:
			q="insert into login values(null,'%s','%s','user')"%(username,password)
			res=insert(q)
			q="insert into user values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,gender,address,phone,email)
			insert(q)
			flash("Register successfully")
	return render_template('user_register.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				flash("Login Successfully")
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="user":
				flash("Login Successfully")
				return redirect(url_for('user.userhome'))
	return render_template('login.html')
