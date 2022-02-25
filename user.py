import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, petID, petName, petOwner, petType):
        self.petID = petID
        self.petName = petName
        self.petOwner = petOwner
        self.petType = petType

@classmethod
def find_by_petid(cls, petID):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "select * from users where petID=?"
    result = cursor.execute(query, (petID,))
    row = result.fetchone()
    if row:
        #user = cls(row[0],row[1], row[2], row[3])
        user = cls(*row)
    else:
        user = None

    connection.close()
    return user 

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

    def delete(self, petID):
        global users
        users = list(filter(lambda x: x['petID'] != petID, users))
        return {'message': 'Item deleted'}

    def put(self, petID):
        data = request.get_json()
        user = next(filter(lambda x: x['petID'] == petID, users), None)
        if user is None:
            user = {'petID': petID,
                    'petName': data['petName'], 
                    'petType': data['petType'],
                    'petOwner': data['petOwner'] 
            }
            users.append(user)
        else:
            user.update(data)
        return user

class Users(Resource):
    def get(self):
        return users
