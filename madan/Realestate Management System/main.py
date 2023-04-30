from flask import Flask
from public import public
from admin import admin
from seller import seller
from user import user
app=Flask(__name__)
app.secret_key="hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(seller,url_prefix='/seller')
app.register_blueprint(user,url_prefix='/user')
app.run(debug=True,port=5013)
