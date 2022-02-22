from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = []

class User(Resource):
    def get(self, petID):
        user = next(filter(lambda x: x['petID'] == petID, users), None)
        return {'user': user}, 200 if user else 404

       

    def post(self, petID):
        if next(filter(lambda x: x['petID'] == petID, users), None):
            return {'message': 'item already exists'}
            
        data = request.get_json()
        user = {'petID': petID,
                'petName': data['petName'], 
                'petType': data['petType'],
                'petOwner': data['petOwner'] }
        users.append(user)
        return user, 201

class Users(Resource):
    def get(self):
        return users

api.add_resource(User, '/user/<string:petID>')
api.add_resource(Users, '/users')

app.run(port=5000, debug=True)
