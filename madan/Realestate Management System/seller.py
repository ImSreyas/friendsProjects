from flask import *
from database import *
import uuid

seller=Blueprint('seller',__name__)

@seller.route('/sellerhome',methods=['get','post'])
def sellerhome():
	return render_template('sellerhome.html')

@seller.route('/manage_contacts',methods=['get','post'])
def manage_contacts():
	data={}
	q="select *,concat(firstname,' ',lastname)as NAME from customer"
	res=select(q)
	data['con']=res
	return render_template('sellermanagecontacts.html',data=data)

@seller.route('/add_property',methods=['get','post'])
def add_property():
	data={}
	ids=session['login_id']
	if 'submit' in request.form:
		cname=request.form['cname']
		image=request.files['image']
		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		amount=request.form['amount']
		des=request.form['des']
		status=request.form['status']
		q="insert into properties values(null,'%s',(select seller_id from seller where login_id='%s'),'%s','%s','%s','%s')"%(cname,ids,path,amount,des,status)
		insert(q)
		flash("Property Added")
	q="select * from category"
	res=select(q)
	data['cat']=res
	return render_template('selleradd_property.html',data=data)


@seller.route('/myproperties',methods=['get','post'])
def myproperties():
	data={}
	ids=session['login_id']
	q="select * from properties where seller_id=(select seller_id from seller where login_id='%s')"%(ids)
	res=select(q)
	data['pr']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from properties where property_id='%s'"%(id)
		delete(q)
		flash("Deleted")
		return redirect(url_for('seller.myproperties'))
	return render_template('sellerview_properties.html',data=data)

@seller.route('/viewreview',methods=['get','post'])
def viewreview():
	data={}
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from feedback inner join customer using(customer_id) where customer_id='%s'"%(id)
	res=select(q)
	data['feed']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" %(reply,res[j]['feedback_id'])
			update(q)
			flash("send message")
			return redirect(url_for('seller.viewreview',id=id))
		j=j+1
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from feedback where feedback_id='%s'"%(id)
		delete(q)
		flash("Feedback Deleted")
		return redirect(url_for('seller.viewreview',id=id))
	return render_template('sellerview_feedbacks.html',data=data)

@seller.route('/viewbooking',methods=['get','post'])
def viewbooking():
	data={}
	id=request.args['id']
	q="select * from booking where property_id='%s'"%(id)
	res=select(q)
	data['book']=res
	return render_template('sellerview_enquires.html',data=data)


@seller.route('/view_enquires',methods=['get','post'])
def view_enquires():
	data={}
	id=request.args['id']
	q="select *,concat(firstname,' ',lastname)as NAME from booking inner join customer using(customer_id) where customer_id='%s'"%(id)
	res=select(q)
	data['book']=res
	if 'id1' in request.args:
		id1=request.args['id1']
		q="update booking set  status='Accept'  where booking_id='%s' and status='booked'"%(id1)
		update(q)
		return redirect(url_for('seller.view_enquires',id=id))
	elif 'id2' in request.args:
		id2=request.args['id2']
		q="update booking set  status='Reject'  where booking_id='%s' and status='booked'"%(id2)
		update(q)
		return redirect(url_for('seller.view_enquires',id=id))
	return render_template('sellerview_booking.html',data=data,id=id)
