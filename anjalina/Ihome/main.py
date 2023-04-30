from flask import *
from public import public
from provider import provider
from admin import admin
from user import user
app=Flask(__name__)
app.secret_key="asddfgh"	
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(provider,url_prefix='/provider')
app.register_blueprint(user,url_prefix='/user')
app.run(debug=True,port=5045)
