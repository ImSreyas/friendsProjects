from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def index():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				flash("Login Successfully")
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=="Customer":
				flash("Login Successfully")
				return redirect(url_for('customer.customerhome'))
			if res[0]['usertype']=="staff":
				flash("Login Successfully")
				return redirect(url_for('staff.staffhome'))
		else:
			flash("Invalid username and password")
	return render_template('login.html')

@public.route('/customer_register',methods=['get','post'])
def customer_register():
	if 'submit' in request.form:
		name=request.form['name']
		age=request.form['age']
		address=request.form['address']
		email=request.form['email']
		phone=request.form['phone']
		place=request.form['place']
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if len(res)>0:
			flash("Already Exists")
		else:
			q="insert into login values(null,'%s','%s','Customer')"%(username,password)
			res=insert(q)
			q="insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,name,age,address,email,phone,place)
			insert(q)
			flash("Registered Successfully")
	return render_template('customer_register.html')