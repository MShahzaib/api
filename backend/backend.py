from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///db.sqlite3')

app = Flask(__name__)
api = Api(app)

class User_get(Resource):
    def get(self):
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from user")
        return {'users': [i[4:6] for i in query.cursor.fetchall()]}

class User_add(Resource):
    def get(self, u, p):
        conn_id = 0
        for _ in open("db_connect"):
            conn_id = int(_)
        conn_id += 1
        with open('db_connect','w') as conn_file:
            conn_file.write(str(conn_id))

        conn = e.connect()
        query = conn.execute("INSERT INTO user (_id,_super,_face,name,username,password) VALUES ('"+str(conn_id)+"','','','','"+u+"','"+p+"')")

        return "{done:true}"
        #query = conn.execute("select * from User where Department='%s'"%department_name.upper())
        #result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        

api.add_resource(User_get, '/user/get')
api.add_resource(User_add,  '/user/add/<string:u>&<string:p>')

if __name__ == '__main__':
     app.run()