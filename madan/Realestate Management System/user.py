from flask import *
from database import*
user=Blueprint('user',__name__)

@user.route('/userhome',methods=['get','post'])
def userhome():
	return render_template('userhome.html')

@user.route('/view_properties',methods=['get','post'])
def view_properties():
	data={}
	q="select *,concat(firstname,' ',lastname)as NAME from properties inner join seller using(seller_id) inner join category using(category_id)"
	res=select(q)
	data['pr']=res
	return render_template('userview_properties.html',data=data)

@user.route('/book_property',methods=['get','post'])
def book_property():
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		date=request.form['date']
		q="insert into booking values(null,'%s',(select customer_id from customer where login_id='%s'),'%s','booked')"%(id,ids,date)
		insert(q)
		flash("Property Booked")
		return redirect(url_for('user.view_properties'))
	return render_template('userbook_property.html')

@user.route('/send_feedbacks',methods=['get','post'])
def send_feedbacks():
	data={}
	ids=session['login_id']
	if 'submit' in request.form:
		feed=request.form['feed']
		q="insert into feedback values(null,(select customer_id from customer where login_id='%s'),'%s','pending',Curdate())"%(ids,feed)
		insert(q)
		flash("Send Feedback")
	q="select *,concat(firstname,' ',lastname)as NAME from feedback inner join customer using(customer_id) where login_id='%s'"%(ids)
	res=select(q)
	data['feed']=res
	return render_template('userfeedback.html',data=data)

@user.route('/my_profile',methods=['get','post'])
def my_profile():
	data={}
	ids=session['login_id']
	q="select *,concat(firstname,' ',lastname)as NAME from customer where login_id='%s'"%(ids)
	res=select(q)
	data['cus']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="update":
		q="select * from customer where customer_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['gender']
		address=request.form['address']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		q="update customer set firstname='%s',lastname='%s',gender='%s',address='%s',place='%s',phone='%s',email='%s' where customer_id='%s'"%(fname,lname,gender,address,place,phone,email,id)
		update(q)
		flash("Profile Updated")
		return redirect(url_for('user.my_profile'))
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1 = select("select login_id from customer where customer_id='%s'" % (id))
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'" % (str(id1[0]['login_id']))
		delete(q)
		q="delete from customer where customer_id='%s'"%(id)
		delete(q)
		flash("Details Deleted")
		return redirect(url_for('user.my_profile'))
	return render_template('userview_myprofile.html',data=data)

@user.route('/change_password',methods=['get','post'])
def change_password():
	ids=session['login_id']
	if 'submit' in request.form:
		password=request.form['password']
		q="update login set password='%s' where  usertype='customer' and login_id='%s'" %(password,ids)
		update(q)
		flash("Your password changed..")
	return render_template('userchange_password.html')

@user.route('/booking_status',methods=['get','post'])
def booking_status():
	data={}
	ids=session['login_id']
	q="select *,concat(firstname,' ',lastname)as NAME from booking inner join customer using(customer_id) where login_id='%s'"%(ids)
	res=select(q)
	data['book']=res
	return render_template('userview_bookingstatus.html',data=data)

@user.route('/make_payment',methods=['get','post'])
def make_payment():
	data={}
	id=request.args['id']
	ids=session['login_id']
	if 'submit' in request.form:
		q="UPDATE `booking` SET status='Paid' WHERE status='Accept'"
		update(q)
		flash("Pay successfully")
		return redirect(url_for('user.booking_status'))
	# else:
	# 	flash("Payment failed")	
	id=request.args['id']	
	q="select * from properties where property_id='%s'"%(id)
	res=select(q)
	data['pay']=res
	return render_template('usermake_payment.html',data=data)