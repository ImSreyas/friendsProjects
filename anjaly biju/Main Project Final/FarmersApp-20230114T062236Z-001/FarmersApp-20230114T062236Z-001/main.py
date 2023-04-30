from flask import Flask
from admin import admin
from officer import officer
from farmer import farmer
from public import public
from technical_wing import technical_wing

app = Flask(__name__)
# when we create a session, a secreat key set.
app.secret_key = "hai"
app.register_blueprint(public)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(officer, url_prefix='/officer')
app.register_blueprint(farmer, url_prefix='/farmer')
app.register_blueprint(technical_wing, url_prefix='/technical_wing')
app.run(debug=True, port=5009)