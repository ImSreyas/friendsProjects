from flask import *
from database import *
import uuid

technical_wing = Blueprint('technical_wing', __name__)


@technical_wing.route('/techhome', methods=['get', 'post'])
def techhome():
    return render_template('techhome.html')


@technical_wing.route('/add_category', methods=['get', 'post'])
def add_category():
    if 'submit' in request.form:
        cname = request.form['cname']
        q = "select * from category where cat_name='%s'" % (cname)
        res = select(q)
        if len(res) > 0:
            flash("Already Exists")
        else:
            q = "insert into category values(null,'%s')" % (cname)
            insert(q)
            flash("Category Added")
    return render_template('techadd_category.html')


@technical_wing.route('/add_product', methods=['get', 'post'])
def add_product():
    data = {}
    q = "select * from category"
    res = select(q)
    data['cat'] = res
    if 'submit' in request.form:
        cname = request.form['cname']
        mname = request.form['mname']
        des = request.form['des']
        amount = request.form['amount']
        image = request.files['img']
        path = 'static/uploads/' + str(uuid.uuid4()) + image.filename
        image.save(path)
        quan = request.form['quan']
        q = "insert into machine values(null,'%s','%s','%s','%s','%s','%s')" % (cname, mname, des, amount, path, quan)
        insert(q)
        flash("Product Added")
    return render_template('techadd_product.html', data=data)


@technical_wing.route('/view_orderedmachine', methods=['get', 'post'])
def view_orderedmachine():
    data = {}
    q = "SELECT *,CONCAT(fname,' ',lname)AS NAME FROM `order_details` INNER JOIN `order_master` USING(om_id)INNER JOIN `machine` USING(machine_id)INNER JOIN farmerregister USING(farmer_id)"
    res = select(q)
    data['order'] = res
    if 'id' in request.args:
        id = request.args['id']
        q = "update order_master set  delivery_status='Order Accept'  where om_id='%s' and delivery_status='pending'" % (
            id)
        update(q)
        return redirect(url_for('technical_wing.view_orderedmachine'))
    elif 'id1' in request.args:
        id1 = request.args['id1']
        q = "update order_master set  delivery_status='Order Reject'  where om_id='%s' and delivery_status='pending'" % (
            id1)
        update(q)
        return redirect(url_for('technical_wing.view_orderedmachine'))
    return render_template('techview_orderedmachine.html', data=data)
