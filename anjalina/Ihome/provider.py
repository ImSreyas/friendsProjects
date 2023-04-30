from flask import *
from database import *
import uuid
provider=Blueprint('provider',__name__)

@provider.route('/providerhome',methods=['get','post'])
def providerhome():
	return render_template("provider_home.html")

@provider.route('/manageservices',methods=['get','post'])
def manageservices():
	data={}
	ids=session['login_id']
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from services where service_id='%s'"%(id)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for("provider.manageservices"))
	if 'submit' in request.form:
		s=request.form['sname']
		sname=request.form['ser']
		# q="insert into services values(null,'%s',(select provider_id from service_provider where login_id='%s'))"%(s,ids)
		q="insert into services values(null,(select provider_id from service_provider where login_id='%s'),'%s','%s')"%(ids,s,sname)
		insert(q)
		flash("inserted successfully")
	q="select * from services inner join service_type using(service_type_id)"
	res=select(q)
	data['servicetypes']=res
	q="select * from service_type"
	res=select(q)
	data['selservicetypes']=res
	return render_template("provider_manage_services.html",data=data)

# # @provider.route('/manageservices',methods=['get','post'])
# # def manageservices():
# # 	data={}
# # 	ids=session['login_id']
# # 	q="select * from service_type"
# # 	res=select(q)
# # 	data['selservicetypes']=res
# # 	if 'action' in request.args:
# # 		action=request.args['action']
# # 		id=request.args['id']
# # 	else:
# # 		action=None
# # 	if action=="delete":
# # 		q="delete from service_type where service_id='%s'"%(id)
# # 		delete(q)
# # 		flash("deleted successfully")
# # 		return redirect(url_for("provider.manageservices"))
# # 	if 'submit' in request.form:
# # 		s=request.form['sname']
# # 		q="insert into services values(null,'%s',(select provider_id from service_provider where login_id='%s'))"%(s,ids)
# # 		insert(q)
# # 		flash("inserted successfully")
# # 	q="select * from service_type inner join service_type using(service_type_id)"
# # 	res=select(q)
# # 	data['servicetypes']=res
# 	return render_template("provider_manage_services.html",data=data)


@provider.route('/viewbooking',methods=['get','post'])
def viewbooking():
	data={}
	id=session['login_id']
	q="SELECT *,concat(users.first_name,' ',users.last_name)as uname FROM  booking inner join users using(user_id) WHERE provider_id=(SELECT provider_id FROM service_provider WHERE login_id='%s')"%(id)
	res=select(q)
	data['viewrequests']=res
	return render_template("provider_view_request.html",data=data)


@provider.route('/sendproposal',methods=['get','post'])
def sendproposal():
	data={}
	bid=request.args['bid']
	id=session['login_id']
	if 'submit' in request.form:
		des=request.form['des']
		amount=request.form['amount']
		q="insert into proposal values(null,'%s','%s','%s',curdate(),'pending')"%(bid,des,amount)
		insert(q)
		flash("proposal send")
	q="SELECT * FROM proposal INNER JOIN booking USING(booking_id) WHERE provider_id=(SELECT provider_id FROM service_provider WHERE login_id='%s')"%(id)
	res=select(q)
	data['viewproposal']=res
	return render_template("provider_send_proposal.html",data=data)

@provider.route('/viewpayment',methods=['get','post'])
def viewpayment():
	data={}
	id=session['login_id']
	pid=request.args['pid']
	q="SELECT * FROM payment WHERE proposal_id='%s'"%(pid)
	res=select(q)
	data['viewpayment']=res
	return render_template("provider_view_payment.html",data=data)

@provider.route('/confirmpay',methods=['get','post'])
def confirmpay():
	data={}
	pid=request.args['pid']
	bid=request.args['bid']
	q="update proposal set status='confirmed' WHERE proposal_id='%s'"%(pid)
	update(q)
	flash("payment confirm")
	return redirect(url_for("provider.sendproposal",bid=bid))
	return render_template("provider_send_proposal.html",data=data)


@provider.route('/viewreviews',methods=['get','post'])
def viewreviews():
	data={}
	id=session['login_id']
	q="SELECT *,concat(users.first_name,' ',users.last_name)as uname FROM ratings inner join users using(user_id) WHERE provider_id=(SELECT provider_id FROM service_provider WHERE login_id='%s')"%(id)
	res=select(q)
	data['viewratings']=res
	return render_template("provider_view_reviews.html",data=data)

@provider.route('/add_shops',methods=['get','post'])
def add_shops():
	ids=session['login_id']
	if 'submit' in request.form:
		shop_name=request.form['shop_name']
		phone=request.form['phone']
		email=request.form['email']
		place=request.form['place']
		q="insert into shop values(null,(select provider_id from service_provider where login_id='%s'),'%s','%s','%s','%s')"%(ids,shop_name,phone,email,place)
		insert(q)
		flash("Shop Added")
	return render_template('provideradd_shops.html')

@provider.route('/add_product',methods=['get','post'])
def add_product():
	ids=session['login_id']
	data={}
	if 'submit' in request.form:
		sname=request.form['sname']
		pname=request.form['pname']
		image=request.files['image']
		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		amount=request.form['amount']
		stock=request.form['stock']
		q="insert into product values(null,'%s','%s','%s','%s','%s')"%(sname,pname,path,amount,stock)
		insert(q)
		flash("Product Added")
	q="select * from shop"
	res=select(q)
	data['sh']=res
	return render_template('provideradd_product.html',data=data)

@provider.route('/view_order',methods=['get','post'])
def view_order():
	data={}
	ids=session['login_id']
	q="SELECT *,CONCAT(service_provider.`first_name`,' ',service_provider.`last_name`)AS SNAME,CONCAT(users.`first_name`,' ',users.`last_name`)AS UNAME FROM order_details INNER JOIN order_master USING(om_id)INNER JOIN users USING(user_id) INNER JOIN product USING(product_id)INNER JOIN shop USING(shop_id)INNER JOIN service_provider USING(provider_id) where provider_id=(select provider_id from service_provider where login_id='%s')"%(ids)
	res=select(q)
	data['or']=res
	if 'id' in request.args:
		id=request.args['id']
		q="update order_master set  delivery_status='Order Accept'  where om_id='%s' and delivery_status='pending'"%(id)
		update(q)
		return redirect(url_for('provider.view_order'))
	elif 'id1' in request.args:
		id1=request.args['id1']
		q="update order_master set  delivery_status='Order Reject'  where om_id='%s' and delivery_status='pending'"%(id1)
		update(q)
		return redirect(url_for('provider.view_order'))
	return render_template('providerview_order.html',data=data)