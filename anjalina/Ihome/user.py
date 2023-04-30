from flask import *
from database import *
import uuid
user=Blueprint('user',__name__)

@user.route('/userhome',methods=['get','post'])
def userhome():
	return render_template('userhome.html')


@user.route('/useradd_request',methods=['get','post'])
def useradd_request():
	data={}
	q="select *,concat(first_name,' ',last_name)as NAME from services inner join service_provider using(provider_id) inner join area using(area_id)"
	res=select(q)
	data['sp']=res
	return render_template('usersend_request.html',data=data)

@user.route('/user_sendrequest',methods=['get','post'])
def user_sendrequest():
	data={}
	ids=session['login_id']
	id=request.args['id']
	id1=request.args['id1']
	if 'submit' in request.form:
		des=request.form['des']
		image=request.files['image']
		path='static/uploads/'+str(uuid.uuid4())+image.filename
		image.save(path)
		image1=request.files['imag']
		path1='static/uploads/'+str(uuid.uuid4())+image1.filename
		image1.save(path1)
		q="insert into booking values(null,(select user_id from users where login_id='%s'),'%s','%s',Curdate(),'booked','%s','%s','%s')"%(ids,id,id1,des,path,path1)
		insert(q)	
	q="SELECT *,CONCAT(service_provider.first_name,service_provider.last_name)AS SNAME,CONCAT(users.first_name,' ',users.last_name)AS UNAME FROM booking INNER JOIN users USING(user_id)INNER JOIN service_provider USING(provider_id)INNER JOIN `area` ON area.area_id = service_provider.area_id  INNER JOIN services USING(service_id) where user_id=(select user_id from users where login_id='%s')"%(ids)
	res=select(q)
	data['book']=res
	return render_template('usersend.html',data=data)

@user.route('/sendcomplaint',methods=['get','post'])
def sendcomplaint():
	data={}
	ids=session['login_id']
	if 'submit' in request.form:
		comp=request.form['comp']
		q="insert into complaints values(null,(select user_id from users where login_id='%s'),'%s','pending',Curdate())"%(ids,comp)
		insert(q)
		flash("Send Complaint")
	q="select *,concat(first_name,' ',last_name)as NAME from complaints inner join users using(user_id) where user_id=(select user_id from users where login_id='%s')"%(ids)
	res=select(q)
	data['compl']=res
	return render_template('usersend_complaint.html',data=data)

@user.route('/userview_product',methods=['get','post'])
def userview_product():
	data={}
	q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM `product` INNER JOIN shop USING(shop_id) INNER JOIN service_provider USING(provider_id)"
	res=select(q)
	data['pr']=res
	return render_template('userview_product.html',data=data)


@user.route('/addratings',methods=['get','post'])
def addratings():
	data={}
	ids=session['login_id']
	if 'submit' in request.form:
		pr=request.form['pname']
		review=request.form['des']
		rate=request.form['rate']
		q="insert into ratings values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',Curdate())"%(ids,pr,review,rate)
		insert(q)
		flash("Add rating")
	q="select *,concat(first_name,' ',last_name)as NAME from service_provider"
	res=select(q)
	data['pro']=res
	return render_template('useradd_rating.html',data=data)


@user.route('/viewproposal',methods=['get','post'])
def viewproposal():
	data={}
	bid=request.args['bid']
	q="SELECT * FROM proposal WHERE booking_id='%s'"%(bid)
	res=select(q)
	data['viewproposal']=res
	return render_template('userview_proposal.html',data=data)


@user.route('/accept',methods=['get','post'])
def accept():
	data={}
	if 'id1' in request.args:
		id1=request.args['id1']
		bid=request.args['bid']
		q="update proposal set status='Accept' where status='pending' and proposal_id='%s'"%(id1)
		update(q)
		flash("Proposal Accepted")
		return redirect(url_for('user.viewproposal',bid=bid))
	q="SELECT * FROM proposal"
	res=select(q)
	data['viewproposal']=res
	return render_template('userview_proposal.html',data=data,bid=bid)


@user.route('/reject',methods=['get','post'])
def reject():
	data={}
	if 'id1' in request.args:
		id1=request.args['id1']
		bid=request.args['bid']
		q="update proposal set status='Reject' where status='pending' and proposal_id='%s'"%(id1)
		update(q)
		flash("Proposal Reject")
		return redirect(url_for('user.useradd_request',bid=bid))
	q="SELECT * FROM proposal"
	res=select(q)
	data['viewproposal']=res
	return render_template('userview_proposal.html',data=data,bid=bid)

@user.route('/make_payment',methods=['get','post'])
def make_payment():
	data={}
	id1=request.args['id1']
	bid=request.args['bid']
	if 'submit' in request.form:
		amt=request.form['am']
		q="insert into payment values(null,'%s','%s',Curdate(),'%s')"%(id1,bid,amt)
		insert(q)
		flash("Pay Successfully")
		return redirect(url_for('user.useradd_request'))
	q="select estimated_amount from proposal"
	res=select(q)
	data['pay']=res
	return render_template('usermake_payment.html',data=data)

@user.route('/get_name',methods=['get','post'])
def get_name():
    class_id=request.args['class_id']
    print(class_id)
    q="select service_name from service where service_id='%s'"%(class_id)
    result=select(q)
    print (result)
    return demjson.encode(result)

@user.route('/addto_cart',methods=['get','post'])
def addto_cart():
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		quantity=request.form['quantity']
		q="insert into cart values(null,(select user_id from users where login_id='%s'),'%s','%s')"%(ids,id,quantity)
		insert(q)
		flash("Quantity Added")
		return redirect(url_for('user.userview_product'))
	return render_template('useraddto_cart.html')


@user.route('/buy_product',methods=['get','post'])
def buy_product():
	data={}
	ids=session['login_id']
	if 'submit' in request.form:
		q="select * from cart inner join users using(user_id) inner join product using(product_id) where user_id=(select user_id from users where login_id='%s')"%(ids)
		res=select(q)
		flag=0
		t_amount=0
		quantity=0
		for range in res:
			product_id=range['product_id']
			quantity=range['quantity']
			costperunit=range['amount']
			total_amount=int(quantity)*int(costperunit)
			if flag==0:
				q="INSERT INTO `order_master` VALUES(NULL,(SELECT user_id FROM users WHERE login_id='%s'),CURDATE(),'pending','0')"%(ids)
				ids=insert(q)
				flag=1  
			q="insert into order_details values(null,'%s','%s','%s','%s','ordered')"%(ids,product_id,quantity,total_amount) 
			insert(q)
			q="update product set stock=stock-'%s' where product_id='%s'"%(quantity,product_id)
			update(q)
		q="update `order_master` set total_amount='%s' where om_id='%s'"%(total_amount,ids)
		update(q)
		q="DELETE FROM cart WHERE user_id=(SELECT user_id FROM users WHERE login_id='%s')"%(ids)
		delete(q)
		flash("Item Ordered")
		return redirect(url_for('user.userview_product'))
	q="SELECT *,CONCAT(first_name, ' ',last_name) AS NAME FROM cart INNER JOIN users USING(user_id) INNER JOIN product USING(product_id)"
	res=select(q)
	data['carts']=res
	return render_template('userbuy_items.html',data=data)


@user.route('/order_status',methods=['get','post'])
def order_status():
	data={}
	ids=session['login_id']
	q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM `order_details` INNER JOIN order_master USING(om_id)INNER JOIN product USING(product_id)INNER JOIN users  USING(user_id) where login_id='%s'"%(ids)
	res=select(q)
	data['or']=res
	return render_template('userorder_status.html',data=data)










