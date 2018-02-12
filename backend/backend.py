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
        return {'users': [i for i in query.cursor.fetchall()]}

class User_add(Resource):
    def get(self,_super,_face,name,username,password):
        conn_id = 0
        for _ in open("db_connect_user"):
            conn_id = int(_)
        conn_id += 1
        with open('db_connect_user','w') as conn_file:
            conn_file.write(str(conn_id))

        conn = e.connect()
        query = conn.execute("INSERT INTO user (_id,_super,_face,name,username,password) VALUES ('"+str(conn_id)+"','"+_super+"','"+_face+"','"+name+"','"+username+"','"+password+"')")

        return "{done:true}"

class User_del(Resource):
    def get(self,_id):
        conn = e.connect()
        query = conn.execute("DELETE FROM user WHERE _id = "+_id)

        return "{done:true}"

#############################################################################################################

class note_get(Resource):
    def get(self):
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from note")
        return {'notes': [i for i in query.cursor.fetchall()]}

class note_add(Resource):
    def get(self,sender,note,_time,receiver_id):
        conn_id = 0
        for _ in open("db_connect_note"):
            conn_id = int(_)
        conn_id += 1
        with open('db_connect_note','w') as conn_file:
            conn_file.write(str(conn_id))

        conn = e.connect()
        query = conn.execute("INSERT INTO note (id,sender,note,'time',receiver_id) VALUES \
            ('"+str(conn_id)+"','"+sender+"','"+note+"','"+_time+"','"+receiver_id+"')")

        return "{done:true}"

class note_del(Resource):
    def get(self,_id):
        conn = e.connect()
        query = conn.execute("DELETE FROM note WHERE id = "+_id)
        return "{done:true}"

#############################################################################################################

class alarm_get(Resource):
    def get(self):
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from alarm")
        return {'alarms': [i for i in query.cursor.fetchall()]}

class alarm_add(Resource):
    def get(self,_time,user_id):
        conn_id = 0
        for _ in open("db_connect_alarm"):
            conn_id = int(_)
        conn_id += 1
        with open('db_connect_alarm','w') as conn_file:
            conn_file.write(str(conn_id))

        conn = e.connect()
        query = conn.execute("INSERT INTO alarm (id,'time',user_id) VALUES \
            ('"+str(conn_id)+"','"+_time+"','"+user_id+"')")

        return "{done:true}"

class alarm_del(Resource):
    def get(self,_id):
        conn = e.connect()
        query = conn.execute("DELETE FROM alarm WHERE id = "+_id)
        return "{done:true}"

#############################################################################################################

class reminder_get(Resource):
    def get(self):
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from reminder")
        return {'reminders': [i for i in query.cursor.fetchall()]}

class reminder_add(Resource):
    def get(self,_time,reminder,user_id):
        conn_id = 0
        for _ in open("db_connect_reminder"):
            conn_id = int(_)
        conn_id += 1
        with open('db_connect_reminder','w') as conn_file:
            conn_file.write(str(conn_id))

        conn = e.connect()
        query = conn.execute("INSERT INTO reminder (id,'time',reminder,user_id) VALUES \
            ('"+str(conn_id)+"','"+_time+"','"+reminder+"','"+user_id+"')")

        return "{done:true}"

class reminder_del(Resource):
    def get(self,_id):
        conn = e.connect()
        query = conn.execute("DELETE FROM reminder WHERE id = "+_id)
        return "{done:true}"

#############################################################################################################

class todo_get(Resource):
    def get(self):
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from todo")
        return {'todos': [i for i in query.cursor.fetchall()]}

class todo_add(Resource):
    def get(self,todo,user_id):
        conn_id = 0
        for _ in open("db_connect_todo"):
            conn_id = int(_)
        conn_id += 1
        with open('db_connect_todo','w') as conn_file:
            conn_file.write(str(conn_id))

        conn = e.connect()
        query = conn.execute("INSERT INTO todo (id,todo,user_id) VALUES \
            ('"+str(conn_id)+"','"+todo+"','"+user_id+"')")

        return "{done:true}"

class todo_del(Resource):
    def get(self,_id):
        conn = e.connect()
        query = conn.execute("DELETE FROM todo WHERE id = "+_id)
        return "{done:true}"


api.add_resource(User_get, '/user/get')
api.add_resource(User_add,  '/user/add/<string:_super>&<string:_face>&<string:name>&<string:username>&<string:password>')
api.add_resource(User_del,  '/user/del/<string:_id>')

api.add_resource(note_get, '/note/get')
api.add_resource(note_add,  '/note/add/<string:sender>&<string:note>&<string:_time>&<string:receiver_id>')
api.add_resource(note_del,  '/note/del/<string:_id>')

api.add_resource(alarm_get, '/alarm/get')
api.add_resource(alarm_add,  '/alarm/add/<string:_time>&<string:user_id>')
api.add_resource(alarm_del,  '/alarm/del/<string:_id>')

api.add_resource(reminder_get, '/reminder/get')
api.add_resource(reminder_add,  '/reminder/add/<string:_time>&<string:reminder>&<string:user_id>')
api.add_resource(reminder_del,  '/reminder/del/<string:_id>')

api.add_resource(todo_get, '/todo/get')
api.add_resource(todo_add,  '/todo/add/<string:todo>&<string:user_id>')
api.add_resource(todo_del,  '/todo/del/<string:_id>')

if __name__ == '__main__':
     app.run()
