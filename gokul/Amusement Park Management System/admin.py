from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')


@admin.route('/view_customers',methods=['get','post'])
def view_customers():
	data={}
	q="select * from customer"
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
		return redirect(url_for('admin.view_customers'))
	return render_template('adminview_customers.html',data=data)

@admin.route('/park_register',methods=['get','post'])
def park_register():
	if 'submit' in request.form:
		park_name=request.form['park_name']
		park_image=request.files['park_image']
		path='static/uploads/'+str(uuid.uuid4())+park_image.filename
		park_image.save(path)
		park_des=request.form['park_des']
		q="insert into park_register values(null,'%s','%s','%s')"%(park_name,path,park_des)
		insert(q)
		flash("Data Added..")
	return render_template('adminadd_parks.html')

@admin.route('/view_parks',methods=['get','post'])
def view_parks():
	data={}
	q="select * from park_register"
	res=select(q)
	data['pa']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from park_register where park_id='%s'"%(id)
		delete(q)
		flash("Data Deleted..")
		return redirect(url_for('admin.view_parks'))
	return render_template('adminview_parks.html',data=data)

@admin.route('/new_rides',methods=['get','post'])
def new_rides():
	id=request.args['id']
	if 'submit' in request.form:
		ride_name=request.form['ride_name']
		ride_des=request.form['ride_des']
		ride_amount=request.form['ride_amount']
		ride_image=request.files['ride_image']
		path='static/uploads/'+str(uuid.uuid4())+ride_image.filename
		ride_image.save(path)
		max_capacity=request.form['max_capacity']
		q="insert into rides values(null,'%s','%s','%s','%s','%s','%s')"%(id,ride_name,ride_des,ride_amount,path,max_capacity)
		insert(q)
		flash("New Ride Added..")
		return redirect(url_for('admin.view_parks'))
	return render_template('adminadd_rides.html')

@admin.route('/add_staff',methods=['get','post'])
def add_staff():
	id=request.args['id']
	if 'submit' in request.form:
		staff_name=request.form['staff_name']
		staff_address=request.form['staff_address']
		staff_email=request.form['staff_email']
		staff_phone=request.form['staff_phone']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','staff')"%(username,password)
		res=insert(q)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s')"%(id,res,staff_name,staff_address,staff_email,staff_phone)
		insert(q)
		flash("New Staff Added..")
		return redirect(url_for('admin.view_parks'))
	return render_template('adminadd_newstaff.html')

@admin.route('/viewreview',methods=['get','post'])
def viewreview():
	data={}
	q="select * from feedback inner join customer using(customer_id)"
	res=select(q)
	data['feed']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" %(reply,res[j]['feedback_id'])
			update(q)
			flash("send message")
			return redirect(url_for('admin.viewreview'))
		j=j+1
	return render_template('adminview_feedback.html',data=data)

@admin.route('/booking_report',methods=['get','post'])
def booking_report():
	data={}
	q="SELECT * FROM `ticket` INNER JOIN `price` USING(price_id)INNER JOIN `customer` USING(customer_id)INNER JOIN rides USING(ride_id) INNER JOIN park_register USING(park_id)"
	res=select(q)
	data['ma']=res
	return render_template('adminview_report.html',data=data)


@admin.route('/view_food',methods=['get','post'])
def view_food():
	data={}
	id=request.args['id']
	q="select * from food_menu inner join park_register using(park_id) where park_id='%s'"%(id)
	res=select(q)
	data['food']=res
	return render_template('adminview_food.html',data=data)