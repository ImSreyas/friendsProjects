from flask import *
from database import *
admin=Blueprint('admin',__name__)
@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')
@admin.route('/adviewservice_providers',methods=['get','post'])
def adviewservice_providers():
	data={}
	# q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM service_provider INNER JOIN areas USING(area_id)"
	q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM `service_provider` INNER JOIN `area` USING(area_id)"
	res=select(q)
	data['ser']=res
	return render_template('adviewservice_provider.html',data=data)	

@admin.route('/adviewusers',methods=['get','post'])
def adviewusers():
	data={}
	# q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM users INNER JOIN areas USING(area_id)"
	q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM users INNER JOIN `area` USING(area_id)" 
	res=select(q)
	data['us']=res
	return render_template('adviewusers.html',data=data)

@admin.route('/adviewbookings',methods=['get','post'])
def adviewbookings():
	data={}
	# q="SELECT *,CONCAT(service_provider.first_name,service_provider.last_name)AS SNAME,CONCAT(users.first_name,' ',users.last_name)AS UNAME FROM bookings INNER JOIN users USING(user_id)INNER JOIN service_provider USING(provider_id)"
	q="SELECT *,CONCAT(service_provider.first_name,service_provider.last_name)AS SNAME,CONCAT(users.first_name,' ',users.last_name)AS UNAME FROM booking INNER JOIN users USING(user_id)INNER JOIN service_provider USING(provider_id)"
	res=select(q)
	data['book']=res
	return render_template('adviewbookings.html')

@admin.route('/adviewpayment',methods=['get','post'])
def adviewpayment():
	data={}
	# q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM payment INNER JOIN proposal USING(proposal.proposal_id)INNER JOIN booking USING(booking.booking_id) INNER JOIN users USING(user_id)"
	q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM payment INNER JOIN booking USING(booking_id) INNER JOIN users USING(user_id)"
	res=select(q)
	data['pay']=res
	return render_template('adviewpayment.html',data=data)

@admin.route('/adviewreviews',methods=['get','post'])
def adviewreviews():
	data={}
	# q="SELECT *,CONCAT(service_provider.first_name,service_provider.last_name)AS SNAME,CONCAT(users.first_name,' ',users.last_name)AS UNAME FROM reviews INNER JOIN users USING(user_id)INNER JOIN service_provider USING(provider_id)"
	q="SELECT *,CONCAT(service_provider.first_name,service_provider.last_name)AS SNAME,CONCAT(users.first_name,' ',users.last_name)AS UNAME FROM ratings INNER JOIN users USING(user_id)INNER JOIN service_provider USING(provider_id)"
	res=select(q)
	data['re']=res
	return render_template('adviewreviews.html',data=data)

@admin.route('/adviewcomplaints',methods=['get','post'])
def adviewcomplaints():
	data={}
	# q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM complaint INNER JOIN users USING(user_id)"
	q="SELECT *,CONCAT(first_name,' ',last_name)AS NAME FROM complaints INNER JOIN users USING(user_id)"
	res=select(q)
	data['com']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE complaints SET reply='%s' WHERE complaint_id='%s'" %(reply,res[j]['complaint_id'])
			update(q)
			return redirect(url_for('admin.adviewcomplaints')) 	
		j=j+1
	return render_template('adviewcomplaints.html',data=data)


@admin.route('/admanagearea',methods=['get','post'])
def admanagearea():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from area where area_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admanagearea'))
	if action=="update":
		q="select * from area where area_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		areaname=request.form['aname']
		area_des=request.form['des']
		q="update area set area_name='%s',area_description='%s' where area_id='%s'"%(areaname,area_des,id)
		update(q)
		return redirect(url_for('admin.admanagearea'))				
	if 'submit' in request.form:
		areaname=request.form['aname']
		area_des=request.form['des']
		q="insert into area values(null,'%s','%s')"%(areaname,area_des)
		insert(q)
	q="select * from area"
	res=select(q)
	data['ara']=res	
	return render_template('admanagearea.html',data=data)

@admin.route('/admanageservicetype',methods=['get','post'])
def admanageservicetype():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from service_type where service_type_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admanageservicetype'))
	if action=="update":
		q="select * from service_type where service_type_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		sname=request.form['sname']
		des=request.form['des']
		q="update service_type set service_type_name='%s',service_type_description='%s' where service_type_id='%s'"%(sname,des,id)
		update(q)
		return redirect(url_for('admin.admanageservicetype'))				
	if 'submit' in request.form:
		sname=request.form['sname']
		des=request.form['des']
		q="insert into service_type values(null,'%s','%s')"%(sname,des)
		insert(q)
	q="select * from service_type"
	res=select(q)
	data['sr']=res	
	return render_template('admanageservices.html',data=data)