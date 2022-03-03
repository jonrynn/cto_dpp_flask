

from flask import Flask
from flask_cors import CORS
from flask_restful import  Api
from user import User, Users


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
CORS(app)
api.add_resource(User, '/user/<string:petID>')
api.add_resource(Users, '/users')

app.run(port=5000, debug=True)
