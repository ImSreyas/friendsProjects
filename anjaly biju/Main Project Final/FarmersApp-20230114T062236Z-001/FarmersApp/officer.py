from flask import *
from database import *
import uuid

officer = Blueprint('officer', __name__)


@officer.route('/officerhome', methods=['get', 'post'])
def officerhome():
    return render_template('officerhome.html')


@officer.route('/view_farmers', methods=['get', 'post'])
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
        return redirect(url_for('officer.view_farmers'))
    return render_template('officerview_farmers.html', data=data)


@officer.route('/view_ideas', methods=['get', 'post'])
def view_ideas():
    data = {}
    q = "select *,concat(fname,' ',lname)as NAME from ideas inner join  farmerregister using(farmer_id)"
    res = select(q)
    data['ide'] = res
    j = 0
    for i in range(1, len(res) + 1):
        if 'submit' + str(i) in request.form:
            reply = request.form['reply' + str(i)]
            q = "UPDATE ideas SET reply='%s' WHERE ideas_id='%s'" % (reply, res[j]['ideas_id'])
            update(q)
            flash("Reply Sended")
            return redirect(url_for('officer.view_ideas'))
        j = j + 1
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None
    if action == "delete":
        q = "delete from ideas where ideas_id='%s'" % (id)
        delete(q)
        return redirect(url_for('officer.view_ideas'))
    return render_template('officerview_ideas.html', data=data)


@officer.route('/manage_tutorials', methods=['get', 'post'])
def manage_tutorials():
    if 'submit' in request.form:
        ids = session['log_id']
        image = request.files['image']
        path = 'static/uploads/' + str(uuid.uuid4()) + image.filename
        image.save(path)
        q = "insert into tutorials values(null,(select officer_id from agriofficer where log_id='%s'),'%s',Curdate())" % (
        ids, path)
        insert(q)
        flash("Tutorials Uploaded")
    return render_template('officermanage_tutorials.html')


@officer.route('/view_enquiry', methods=['get', 'post'])
def view_enquiry():
    data = {}
    q = "select *,concat(fname,' ',lname)as NAME from enquiry inner join  farmerregister using(farmer_id)"
    res = select(q)
    data['ide'] = res
    j = 0
    for i in range(1, len(res) + 1):
        if 'submit' + str(i) in request.form:
            reply = request.form['reply' + str(i)]
            q = "UPDATE enquiry SET reply='%s' WHERE enquiry_id='%s'" % (reply, res[j]['enquiry_id'])
            update(q)
            flash("Reply Sended")
            return redirect(url_for('officer.view_enquiry'))
        j = j + 1
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None
    if action == "delete":
        q = "delete from enquiry where enquiry_id='%s'" % (id)
        delete(q)
        return redirect(url_for('officer.view_ideas'))
    return render_template('officerview_enquiry.html', data=data)
