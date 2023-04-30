from flask import *
from database import *
farmer=Blueprint('farmer',__name__)
@farmer.route('/farmerhome',methods=['get','post'])
def farmerhome():
	return render_template('farmerhome.html')
@farmer.route('/farviewnotify',methods=['get','post'])
def farviewnotify():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if 	action=="delete":
		q="delete from notification where notify_id='%s'"%(id)
		delete(q)
		flash("successfully deleted")
		return redirect(url_for('farmer.farviewnotify'))
	q="select * from notification"
	res=select(q)
	data['notification']=res
	return render_template('farmerview_notify.html',data=data)

@farmer.route('/view_crops',methods=['get','post'])
def view_crops():
	data={}
	q="select * from crop"
	res=select(q)
	data['cr']=res
	return render_template('farmerview_crops.html',data=data)

@farmer.route('/view_soiltypes',methods=['get','post'])
def view_soiltypes():
	data={}
	q="select * from soil_type"
	res=select(q)
	data['so']=res
	return render_template('farmerview_soiltypes.html',data=data)

@farmer.route('/view_fertilisers',methods=['get','post'])
def view_fertilisers():
	data={}
	q="select * from fertiliser"
	res=select(q)
	data['fer']=res
	return render_template('farmerview_fertilisers.html',data=data)

@farmer.route('/view_tutorials',methods=['get','post'])
def view_tutorials():
	data={}
	q="select * from tutorials"
	res=select(q)
	data['to']=res
	return render_template('farmerview_tutorials.html',data=data)

@farmer.route('/send_complaint',methods=['get','post'])
def send_complaint():
	ids=session['log_id']
	if 'submit' in request.form:
		complaint=request.form['des']
		q="insert into complaints values(null,(select farmer_id from farmerregister where log_id='%s'),'%s','pending',Curdate())"%(ids,complaint)
		insert(q)
		flash("Complaint Send")
	return render_template('farmersend_complaint.html')

@farmer.route('/view_reply',methods=['get','post'])
def view_reply():
	data={}
	ids=session['log_id']
	q="select *,concat(fname,' ',lname)as NAME from complaints inner join farmerregister using(farmer_id) where log_id='%s'"%(ids)
	res=select(q)
	data['com']=res
	return render_template('farmerview_reply.html',data=data)

@farmer.route('/search_officer',methods=['get','post'])
def search_officer():
	data={}
	if 'submit' in request.form:        
		place=request.form['name']
		q="select *,concat(fname,' ',lname)as NAME from agriofficer inner join agridepartment using(dep_id) WHERE  agriofficer.place LIKE '%s'"%(place)
		res=select(q)
		data['viewsearch']=res
	return render_template('farmersearch_officer.html',data=data)

@farmer.route('/send_suggestions',methods=['get','post'])
def send_suggestions():
	id=request.args['id']
	ids=session['log_id']
	if 'submit' in request.form:
		message=request.form['des']
		q="insert into ideas values(null,(select farmer_id from farmerregister where log_id='%s'),'%s','%s','pending',Curdate())"%(ids,id,message)
		insert(q)
		flash("Message send..")
		return redirect(url_for('farmer.search_officer'))
	return render_template('farmersend_suggessions.html')

@farmer.route('/enquiry',methods=['get','post'])
def enquiry():
	id=request.args['id']
	ids=session['log_id']
	if 'submit' in request.form:
		message=request.form['des']
		q="insert into enquiry values(null,(select farmer_id from farmerregister where log_id='%s'),'%s','%s','pending',Curdate())"%(ids,id,message)
		insert(q)
		flash("Message send..")
		return redirect(url_for('farmer.search_officer'))
	return render_template('farmersend_enquiry.html')

@farmer.route('/view_ideas',methods=['get','post'])
def view_ideas():
	data={}
	ids=session['log_id']
	q="select *,concat(fname,' ',lname)as NAME from ideas inner join  farmerregister using(farmer_id) where log_id='%s'"%(ids)
	res=select(q)
	data['ide']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from ideas where ideas_id='%s'"%(id)
		delete(q)
		return redirect(url_for('farmer.view_ideas'))
	return render_template('farmerview_ideasreply.html',data=data)


@farmer.route('/view_enquiry',methods=['get','post'])
def view_enquiry():
	data={}
	ids=session['log_id']
	q="select *,concat(fname,' ',lname)as NAME from enquiry inner join  farmerregister using(farmer_id) where log_id='%s'"%(ids)
	res=select(q)
	data['ide']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from enquiry where enquiry_id='%s'"%(id)
		delete(q)
		return redirect(url_for('farmer.view_enquiry'))
	return render_template('farmerview_enquiryreply.html',data=data)

@farmer.route('/view_product',methods=['get','post'])
def view_product():
	data={}
	q="select * from machine"
	res=select(q)
	data['mach']=res
	return render_template('farmerview_machine.html',data=data)

@farmer.route('/prodetails',methods=['get','post'])
def prodetails():
	data={}
	id=request.args['id']
	q="select * from machine where machine_id='%s'"%(id)
	res=select(q)
	data['mach']=res
	return render_template('farmerviewmachine.html',data=data)

@farmer.route('/addtocart',methods=['get','post'])
def addtocart():
	ids=session['log_id']
	id=request.args['id']
	if 'submit' in request.form:
		quan=request.form['quan']
		q="insert into cart values(null,(select farmer_id from farmerregister where log_id='%s'),'%s','%s')"%(ids,id,quan)
		insert(q)
		flash("Quntity Added")
		return redirect(url_for('farmer.view_product'))
	return render_template('farmeraddto_cart.html')

@farmer.route('/buy_product',methods=['get','post'])
def buy_product():
	data={}
	ids=session['log_id']
	if 'submit' in request.form:
		q="select * from cart inner join farmerregister using(farmer_id) inner join machine using(machine_id) where farmer_id=(select farmer_id from farmerregister where log_id='%s')"%(ids)
		res=select(q)
		flag=0
		t_amount=0
		quantity=0
		for range in res:
			machine_id=range['machine_id']
			quantity=range['quantity']
			costperunit=range['amount']
			total_amount=int(quantity)*int(costperunit)
			if flag==0:
				q="INSERT INTO `order_master` VALUES(NULL,(SELECT farmer_id FROM farmerregister WHERE log_id='%s'),CURDATE(),'pending','0')"%(ids)
				ids=insert(q)
				flag=1
			q="insert into order_details values(null,'%s','%s','%s','%s','ordered')"%(ids,machine_id,quantity,total_amount) 
			insert(q)
			q="update machine set aval_quantity=aval_quantity-'%s' where machine_id='%s'"%(quantity,machine_id)
			update(q)
		q="update `order_master` set total_amount='%s' where om_id='%s'"%(total_amount,ids)
		update(q)
		q="DELETE FROM cart WHERE farmer_id=(SELECT farmer_id FROM farmerregister WHERE log_id='%s') and machine_id='%s'"%(ids,id)
		delete(q)
		flash("Machine Ordered")
		return redirect(url_for('farmer.view_product'))  
	q="SELECT *,CONCAT(fname, ' ',lname) AS NAME FROM cart INNER JOIN farmerregister USING(farmer_id) INNER JOIN machine USING(machine_id)"
	res=select(q)
	data['carts']=res
	return render_template('farmerbuy_product.html',data=data)

@farmer.route('/delivery_status',methods=['get','post'])
def delivery_status():
    data={}
    ids=session['log_id']
    q="SELECT *,CONCAT(fname,' ',lname)AS NAME FROM `order_details` INNER JOIN `order_master` USING(om_id)INNER JOIN `machine` USING(machine_id)INNER JOIN farmerregister USING(farmer_id) WHERE log_id='%s'"%(ids)
    res=select(q)
    data['order']=res
    return render_template('farmerview_deliverystatus.html',data=data)

@farmer.route('/upload',methods=['get','post'])
def upload():
    # if request.method == 'POST':
    #     # Get the file from post request
    #     f = request.files['file']

    #     # Save the file to ./uploads
    #     basepath = os.path.dirname(__file__)
    #     file_path = os.path.join(
    #         basepath, 'uploads', secure_filename(f.filename))
    #     f.save(file_path)

    #     # Make prediction
    #     preds = model_predict(file_path, model)
    #     print(preds[0])

    #     # x = x.reshape([64, 64]);
    #     disease_class = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
    #                      'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
    #                      'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
    #                      'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
    #                      'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
    #     a = preds[0]
    #     ind=np.argmax(a)
    #     print('Prediction:', disease_class[ind])
    #     result=disease_class[ind]
    #     return result
    # 	return None

	return render_template("farmer_predict_disese.html")