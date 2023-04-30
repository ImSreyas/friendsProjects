from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/customerhome',methods=['get','post'])
def customerhome():
	return render_template('customerhome.html')


@customer.route('/profile',methods=['get','post'])
def profile():
	data={}
	ids=session['login_id']
	q="select * from customer where login_id='%s'"%(ids)
	res=select(q)
	data['cus']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		q="delete from customer where customer_id='%s'"%(id)
		delete(q)
		flash("Account Deleted..")
		return redirect(url_for('public.customer_register'))
	if action=="update":
		q="select * from customer where customer_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		name=request.form['name']
		age=request.form['age']
		address=request.form['address']
		email=request.form['email']
		phone=request.form['phone']
		place=request.form['place']
		q="update customer set name='%s',age='%s',address='%s',email='%s',phone='%s',place='%s' where customer_id='%s'"%(name,age,address,email,phone,place,id)
		update(q)
		flash("Profile Updated")
		return redirect(url_for('customer.profile'))
	return render_template('customerview_profile.html',data=data)

@customer.route('/send_feedback',methods=['get','post'])
def send_feedback():
	ids=session['login_id']
	if 'submit' in request.form:
		feed=request.form['feed']
		q="insert into feedback values(null,(select customer_id from customer where login_id='%s'),'%s','Pending',Curdate())"%(ids,feed)
		insert(q)
		flash("Feedback Added..")
		return redirect(url_for('customer.customerhome'))
	return render_template('customersend_feedback.html')

@customer.route('/view_responses',methods=['get','post'])
def view_responses():
	data={}
	q="select * from feedback inner join customer using(customer_id)"
	res=select(q)
	data['feed']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from feedback where feedback_id='%s'"%(id)
		delete(q)
		flash("Feedback Deleted..")
		return redirect(url_for('customer.view_responses'))
	return render_template('customerview_responses.html',data=data)

@customer.route('/view_parks',methods=['get','post'])
def view_parks():
	data={}
	q="select * from park_register"
	res=select(q)
	data['park']=res
	return render_template('customerview_parks.html',data=data)

@customer.route('/view_rides',methods=['get','post'])
def view_rides():
	data={}
	q="select * from rides inner join park_register using(park_id)"
	res=select(q)
	data['ride']=res
	return render_template('customerview_rides.html',data=data)

@customer.route('/view_price',methods=['get','post'])
def view_price():
	data={}
	q="select * from price inner join rides using(ride_id) inner join park_register using(park_id)"
	res=select(q)
	data['price']=res
	return render_template('customerview_price.html',data=data)

@customer.route('/book_ticket',methods=['get','post'])
def book_ticket():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select * from price where price_id='%s'"%(id)
	res=select(q)
	data['updateprt']=res
	if 'submit' in request.form:
		ids=session['login_id']
		id=request.args['id']
		quantity=request.form['quantity']
		total_amount=int(res[0]['new_price'])*int(quantity)
		q="insert into ticket values(null,'%s',(select customer_id from customer where login_id='%s'),'Pending','%s','%s')"%(id,ids,quantity,total_amount)
		insert(q)
		flash("Ticket Booked Successfully..")
		return redirect(url_for('customer.view_price'))
	return render_template('customerbook_ticket.html',data=data)

@customer.route('/make_payment',methods=['get','post'])
def make_payment():
	data={}
	id=request.args['id']
	ids=session['login_id']
	q="SELECT * FROM `ticket` INNER JOIN `price` USING(price_id)INNER JOIN `customer` USING(customer_id)INNER JOIN rides USING(ride_id) INNER JOIN park_register USING(park_id) where login_id='%s' and price_id='%s'"%(ids,id)
	res=select(q)
	data['ma']=res
	return render_template('customerview_paymentstatus.html',data=data)

@customer.route('/view_food',methods=['get','post'])
def view_food():
	data={}
	q="select * from food_menu inner join park_register using(park_id)"
	res=select(q)
	data['food']=res
	return render_template('customerview_food.html',data=data)


@customer.route('/food_ordering',methods=['get','post'])
def food_ordering():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select * from food_menu where food_id='%s'"%(id)
	res=select(q)
	data['updateprt']=res
	if 'submit' in request.form:
		ids=session['login_id']
		id=request.args['id']
		quantity=request.form['quantity']
		total_amount=int(res[0]['price'])*int(quantity)
		q="insert into food_order values(null,'%s',(select customer_id from customer where login_id='%s'),'Pending','%s','%s')"%(id,ids,quantity,total_amount)
		insert(q)
		flash("Food Ordered..")
		return redirect(url_for('customer.view_food'))
	return render_template('customerorder_food.html',data=data)


@customer.route('/order_status',methods=['get','post'])
def order_status():
	data={}
	id=request.args['id']
	ids=session['login_id']
	q="SELECT * FROM `food_order` INNER JOIN `food_menu` USING(food_id)INNER JOIN `customer` USING(customer_id)INNER JOIN park_register USING(park_id) where login_id='%s' and food_id='%s'"%(ids,id)
	res=select(q)
	data['ma']=res
	return render_template('customerview_orderstatus.html',data=data)
