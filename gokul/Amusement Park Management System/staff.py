from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/staffhome',methods=['get','post'])
def staffhome():
	return render_template('staffhome.html')

@staff.route('/view_responses',methods=['get','post'])
def view_responses():
	data={}
	q="select * from feedback inner join customer using(customer_id)"
	res=select(q)
	data['feed']=res
	return render_template('staffview_responses.html',data=data)

@staff.route('/manage_ridelist',methods=['get','post'])
def manage_ridelist():
	data={}
	ids=session['login_id']
	q="select * from staff inner join park_register using(park_id) where login_id='%s'"%(ids)
	res=select(q)
	data['ri']=res
	return render_template('staffmanage_ridelist.html',data=data)

@staff.route('/view_rides',methods=['get','post'])
def view_rides():
	data={}
	id=request.args['id']
	q="select * from rides inner join park_register using(park_id) where park_id='%s'"%(id)
	res=select(q)
	data['rl']=res
	return render_template('staffview_rides.html',data=data)

@staff.route('/new_price',methods=['get','post'])
def new_price():
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		new_price=request.form['new_price']
		start_date=request.form['start_date']
		end_date=request.form['end_date']
		q="insert into price values(null,(select staff_id from staff where login_id='%s'),'%s','%s','%s','%s')"%(ids,id,new_price,start_date,end_date)
		insert(q)
		flash("New Price Added..")
	return render_template('staffnew_price.html')

@staff.route('/view_pricelist',methods=['get','post'])
def view_pricelist():
	data={}
	ids=session['login_id']
	q="SELECT * FROM `price` INNER JOIN `rides` USING(ride_id)INNER JOIN park_register USING(park_id) INNER JOIN staff USING(staff_id) where login_id='%s'"%(ids)
	res=select(q)
	data['pr']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from price where price_id='%s'"%(id)
		delete(q)
		flash("Offer Removed..")
		return redirect(url_for('staff.view_pricelist'))
	return render_template('staffview_pricelist.html',data=data)

@staff.route('/view_booking',methods=['get','post'])
def view_booking():
	data={}
	ids=session['login_id']
	q="SELECT * FROM `ticket` INNER JOIN `price` USING(price_id)INNER JOIN `customer` USING(customer_id)INNER JOIN rides USING(ride_id) INNER JOIN park_register USING(park_id) inner join staff using(staff_id) where staff_id=(select staff_id from staff where login_id='%s')"%(ids)
	res=select(q)
	data['ma']=res
	if 'id' in request.args:
		id=request.args['id']
		q="update ticket set  ticket_status='Booking Accept'  where ticket_id='%s' and ticket_status='Pending'"%(id)
		update(q)
		return redirect(url_for('staff.view_booking'))
	elif 'id1' in request.args:
		id1=request.args['id1']
		q="update ticket set  ticket_status='Booking Reject'  where ticket_id='%s' and ticket_status='Pending'"%(id1)
		update(q)
		return redirect(url_for('staff.view_booking'))
	return render_template('staffview_bookingstatus.html',data=data)


@staff.route('/food_menu',methods=['get','post'])
def food_menu():
	id=request.args['id']
	if 'submit' in request.form:
		food_name=request.form['food_name']
		price=request.form['price']
		image=request.files['image']
		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		q="insert into food_menu values(null,'%s','%s','%s','%s')"%(id,food_name,price,path)
		insert(q)
		flash("Food Added")
	return render_template('staffadd_fooddetails.html')

@staff.route('/view_food',methods=['get','post'])
def view_food():
	data={}
	id=request.args['id']
	q="select * from food_menu inner join park_register using(park_id) where park_id='%s'"%(id)
	res=select(q)
	data['food']=res
	return render_template('staffview_food.html',data=data)

@staff.route('/order_status',methods=['get','post'])
def order_status():
	data={}
	id=request.args['id']
	q="SELECT * FROM `food_order` INNER JOIN `food_menu` USING(food_id)INNER JOIN `customer` USING(customer_id)INNER JOIN park_register USING(park_id) where  food_id='%s'"%(id)
	res=select(q)
	data['ma']=res
	if 'id1' in request.args:
		id1=request.args['id1']
		q="update food_order set order_status='Order Accept'  where fd_id='%s' and order_status='Pending'"%(id1)
		update(q)
		return redirect(url_for('staff.order_status',id=id))
	elif 'id2' in request.args:
		id2=request.args['id2']
		q="update food_order set order_status='Order Reject'  where fd_id='%s' and order_status='Pending'"%(id2)
		update(q)
		return redirect(url_for('staff.order_status',id=id))
	return render_template('staffview_orderstatus.html',data=data,id=id)


