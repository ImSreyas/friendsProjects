from flask import *
from database import *
public=Blueprint('public',__name__)
@public.route('/',methods=['get','post'])
def publichome():
    
	return render_template('index.html')

@public.route('/farmer_register',methods=['get','post'])
def farmer_reg():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if 	action=="delete":
		q="delete from farmerregister where farmer_id='%s'"%(id)
		delete(q)
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		address=request.form['address']
		gender=request.form['gender']
		place=request.form['place']
		district=request.form['district']
		state=request.form['state']
		country=request.form['country']
		pincode=request.form['pincode']
		phone=request.form['phone']
		uname=request.form['uname']
		password=request.form['password']
		q="select username,password from login where username='%s' and password='%s'" %(uname,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
			# return render_template('farmerregister.html')
		else:
			q="insert into login values(null,'%s','%s','farmer')"%(uname,password)
			id=insert(q)
			q="insert into farmerregister values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,address,gender,place,district,state,country,pincode,phone)
			result=insert(q)	    
			flash("Register successfully")
			# return redirect(url_for('/.login'))
	# return render_template(url_for('index.html'))
	# q="select * from farmerregister"
	# res=select(q)
	# data['reg']=ress	
	return render_template('farmer_register.html',data=data)	
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		u=request.form['uname']
		p=request.form['password']
		q="select * from login where username='%s' and password='%s'" %(u,p)
		result=select(q)
		flash("successfully login")
		if result:
			session['log_id']=result[0]['log_id']
			if result[0]['type']=="admin":
				return redirect(url_for('admin.admins'))
			if result[0]['type']=="Officer":
				return redirect(url_for('officer.officerhome'))
			if result[0]['type']=="farmer":
				return redirect(url_for('farmer.farmerhome'))
			if result[0]['type']=="dealer":
				return redirect(url_for('technical_wing.techhome'))	
		else:
			flash("invalid username and password")
	# 		return redirect(url_for('index.html'))												
	return render_template('login.html')
@public.route('/notification',methods=['get','post'])	
def notification():
	data={}
	q="select * from notification"
	res=select(q)
	data['notification']=res
	return render_template('publicviewnoti.html',data=data)


@public.route('/tech_register',methods=['get','post'])
def tech_register():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		address=request.form['address']
		gender=request.form['gender']
		place=request.form['place']
		district=request.form['district']
		state=request.form['state']
		country=request.form['country']
		pincode=request.form['pincode']
		phone=request.form['phone']
		uname=request.form['uname']
		password=request.form['password']
		q="select username,password from login where username='%s' and password='%s'" %(uname,password)
		print(q)
		result=select(q)
		if len(result)>0:
			flash("That username and password is already exist")
			# return render_template('farmerregister.html')
		else:
			q="insert into login values(null,'%s','%s','dealer')"%(uname,password)
			id=insert(q)
			q="insert into technicalregisters values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,address,gender,place,district,state,country,pincode,phone)
			result=insert(q)	    
			flash("Register successfully")
	return render_template('tec_register.html')


	
	
  		





