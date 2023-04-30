from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/view_feedback',methods=['get','post'])
def view_feedback():
	data={}
	q="select *,concat(fname,' ',lname)as NAME from feedback inner join user using(user_id)"
	res=select(q)
	data['feed']=res
	j=0
	for i in range(1,len(res)+1):
		if 'submit' + str(i) in request.form:
			reply=request.form['reply'+str(i)]
			q="UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" %(reply,res[j]['feedback_id'])
			update(q)
			flash("send message")
			return redirect(url_for('admin.view_feedback'))
		j=j+1
	return render_template('adminview_feedback.html',data=data)

@admin.route('/view_users',methods=['get','post'])
def view_users():
	data={}
	q="select *,concat(fname,' ',lname)as NAME from user"
	res=select(q)
	data['us']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		q="delete from user where user_id='%s'"%(id)
		delete(q)
		flash("Account Deleted")
		return redirect(url_for('admin.adminhome'))
	return render_template('adminview_users.html',data=data)