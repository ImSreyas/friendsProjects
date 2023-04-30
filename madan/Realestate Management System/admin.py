from flask import *
from database import*
admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/addcategory',methods=['get','post'])
def addcategory():
	if 'submit' in request.form:
		catname=request.form['cat_name']
		description=request.form['cat_desc']
		q="select * from category where cat_name='%s'"%(catname)
		res=select(q)
		if len(res)>0:
			flash("The Category Is Already Exists")
		else:
			q="insert into category values(null,'%s','%s')"%(catname,description)
			insert(q)
			flash("Category Added")
	return render_template('adminaddcategory.html')

@admin.route('/addstate',methods=['get','post'])
def addstate():
	if 'submit' in request.form:
		state=request.form['state']
		country=request.form['country']
		city=request.form['city']
		q="select * from state where state='%s'"%(state)
		res=select(q)
		if len(res)>0:
			flash("The State Is Already Exists")
		else:
			q="insert into state values(null,'%s','%s','%s')"%(state,country,city)
			insert(q)
			flash("Details Added")
	return render_template('adminaddstate.html')

@admin.route('/view_users',methods=['get','post'])
def view_users():
	data={}
	q="select *,concat(firstname,' ',lastname)as NAME from customer"
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
		flash("Details Deleted")
		return redirect(url_for('admin.view_users'))
	return render_template('adminview_users.html',data=data)

@admin.route('/view_owners',methods=['get','post'])
def view_owners():
	data={}
	q="select *,concat(firstname,' ',lastname)as NAME from seller"
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
		q="delete from seller where seller_id='%s'"%(id)
		delete(q)
		flash("Details Deleted")
		return redirect(url_for('admin.view_seller'))
	return render_template('adminview_seller.html',data=data)

@admin.route('/view_reviews',methods=['get','post'])
def view_reviews():
    data={}
    q="select *,concat(firstname,' ',lastname)as NAME from feedback inner join customer using(customer_id)"
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
        flash("Feedback Deleted")
        return redirect(url_for('admin.view_reviews'))
    return render_template('adminview_reviews.html',data=data)
