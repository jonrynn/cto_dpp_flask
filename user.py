import sqlite3

from flask_restful import Resource, reqparse





class User(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('petName')
    parser.add_argument('petOwner' )
    parser.add_argument('petType')

    def get(self, petID):
        user = self.find_by_petID(petID)
        if user:
            return user
        return {'message': 'User not found'}, 404

    @classmethod
    def find_by_petID(cls, petID):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "select * from users where petID=?"
        result = cursor.execute(query, (petID,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'petID': row[0], 'petName': row[1], 'petOwner': row[2], 'petType': row[3]}}


    

    def post(self, petID):
        if self.find_by_petID(petID):
            return {'message': "A user with petID '{}' already exists.".format(petID)}

        data = User.parser.parse_args()
        

        user = {'petID': petID, 'petName': data['petName'], 'petOwner':data['petOwner'], 'petType': data['petType']}
        
        #try:
        User.insert(user)
        #except:
        #    return {"message": "An error occurred inserting the user."}

        return user

    @classmethod
    def insert(cls, user):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES(?, ?,?,?)"
        cursor.execute(query, (user['petID'], user['petName'], user['petOwner'], user['petType']))

        connection.commit()
        connection.close()


    def delete(self, petID):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM users WHERE petID=?"
        cursor.execute(query, (petID,))

        connection.commit()
        connection.close()

        return {'message': 'user deleted'}


    def put(self, petID):
        data = User.parser.parse_args()
        user = self.find_by_petID(petID)
        updated_user = {'petID': petID, 'petName': data['petName'], 'petOwner':data['petOwner'], 'petType': data['petType']}
  
        if user is None:
            try:
                User.insert(updated_user)
            except:
                return {"message": "An error occurred inserting the user."}
        else:
            try:
                User.update(updated_user)
            except:
                return {"message": "An error occurred updating the user."}
        return updated_user

    @classmethod
    def update(cls, user):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE users SET petName=?, petOwner=?,petType=? WHERE petID=?"
        cursor.execute(query, ( user['petName'], user['petOwner'], user['petType'],user['petID']))

        connection.commit()
        connection.close()




class Users(Resource):
     def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users"
        result = cursor.execute(query)
        users = []
        for row in result:
            users.append({'petID': row[0], 'petName': row[1], 'petOwner': row[2], 'petType': row[3]})
        connection.close()
#/Users/jonathanrynn/VSCode/cto_flask_venv/code/app.py
        return {"users": users}
