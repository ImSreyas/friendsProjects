from flask import Blueprint, request, render_template, url_for, redirect, session, flash
from database import *

admin = Blueprint('admin', __name__)


@admin.route('/admins', methods=['get', 'post'])
def admins():
    return render_template('adminhome.html')


@admin.route('/manage_department', methods=['get', 'post'])
def manage_department():
    if 'submit' in request.form:
        dname = request.form['dname']
        des = request.form['des']
        q = "select * from agridepartment where dep_name='%s'" % (dname)
        res = select(q)
        if len(res) > 0:
            flash("Already Exists")
        else:
            q = "insert into agridepartment values(null,'%s','%s')" % (dname, des)
            insert(q)
            flash("Department added")
    return render_template('admanage_department.html')


@admin.route('/manage_officers', methods=['get', 'post'])
def manage_officers():
    data = {}
    q = "select * from agridepartment"
    res = select(q)
    data['dep'] = res
    if 'submit' in request.form:
        dname = request.form['dname']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        address = request.form['address']
        place = request.form['place']
        phone = request.form['phone']
        email = request.form['email']
        uname = request.form['uname']
        password = request.form['password']
        q = "select * from login where username='%s' and password='%s'" % (uname, password)
        result = select(q)
        if len(result) > 0:
            flash("That username and password is already exist")
        # return render_template('farmerregister.html')
        else:
            q = "insert into login values(null,'%s','%s','Officer')" % (uname, password)
            res = insert(q)
            q = "insert into agriofficer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            res, dname, fname, lname, gender, address, place, phone, email)
            insert(q)
            flash("Officeres Registered")
    return render_template('admanage_officers.html', data=data)


@admin.route('/manage_newnotification', methods=['get', 'post'])
def manage_newnotification():
    if 'submit' in request.form:
        news = request.form['news']
        date = request.form['date']
        q = "insert into notification values(null,'%s','%s')" % (news, date)
        insert(q)
        flash("New Notification Added")
    return render_template('admanage_notinews.html')


@admin.route('/manage_croptype', methods=['get', 'post'])
def manage_croptype():
    if 'submit' in request.form:
        cname = request.form['cname']
        des = request.form['des']
        q = "select * from crop where crop_name='%s'" % (cname)
        res = select(q)
        if len(res) > 0:
            flash("Already Exists")
        else:
            q = "insert into crop values(null,'%s','%s')" % (cname, des)
            insert(q)
            flash("CropType added")
    return render_template('admanage_croptypes.html')


@admin.route('/manage_soiltype', methods=['get', 'post'])
def manage_soiltype():
    if 'submit' in request.form:
        sname = request.form['sname']
        des = request.form['des']
        q = "select * from soil_type where soil_type_name='%s'" % (sname)
        res = select(q)
        if len(res) > 0:
            flash("Already Exists")
        else:
            q = "insert into soil_type values(null,'%s','%s')" % (sname, des)
            insert(q)
            flash("SoilType added")
    return render_template('admanage_soiltypes.html')


@admin.route('/manage_fertiliser', methods=['get', 'post'])
def manage_fertiliser():
    if 'submit' in request.form:
        fname = request.form['fname']
        des = request.form['des']
        features = request.form['fea']
        q = "select * from fertiliser where fertiliser_name='%s'" % (fname)
        res = select(q)
        if len(res) > 0:
            flash("Already Exists")
        else:
            q = "insert into fertiliser values(null,'%s','%s','%s')" % (fname, des, features)
            insert(q)
            flash("Fertiliser Added")
    return render_template('admanage_fertilisers.html')


@admin.route('/view_farmers', methods=['get', 'post'])
def view_farmers():
    data = {}
    q = "select *,concat(fname,' ',lname)as NAME from farmerregister"
    res = select(q)
    data['fam'] = res
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
        id1 = request.args['id1']
    else:
        action = None
    if action == "delete":
        q = "delete from login where log_id='%s'" % (id1)
        delete(q)
        q = "delete from farmerregister where farmer_id='%s'" % (id)
        delete(q)
        return redirect(url_for('admin.view_farmers'))
    return render_template('adview_farmers.html', data=data)


@admin.route('/view_complaints', methods=['get', 'post'])
def view_complaints():
    data = {}
    q = "select *,concat(fname,' ',lname)as NAME from complaints inner join farmerregister using(farmer_id)"
    res = select(q)
    data['comp'] = res
    j = 0
    for i in range(1, len(res) + 1):
        if 'submit' + str(i) in request.form:
            reply = request.form['reply' + str(i)]
            q = "UPDATE complaints SET reply='%s' WHERE complaint_id='%s'" % (reply, res[j]['complaint_id'])
            update(q)
            flash("Reply Sended")
            return redirect(url_for('admin.view_complaints'))
        j = j + 1
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None
    if action == "delete":
        q = "delete from complaints where complaint_id='%s'" % (id)
        delete(q)
        flash("Complaint Deleted")
        return redirect(url_for('admin.view_complaints'))
    return render_template('adview_complaints.html', data=data)
