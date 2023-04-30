from flask import Flask
from public import public
from admin import admin
from staff import staff
from customer import customer
app=Flask(__name__)
app.secret_key="Hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(customer,url_prefix='/customer')
app.run(debug="True",port=5055)