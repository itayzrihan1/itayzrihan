import requests, pymysql, datetime, json, flask
from flask import Flask, request
app = Flask(__name__)

# local users storage
users = {}



# supported methods
@app.route('/dogs/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def dogs():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 12F1HSutPL.dogs;")
    r = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(r), 200 # status code


# todo elif for put and delete


app.run(host='127.0.0.1', debug=True, port=5000)




res = requests.post('http://127.0.0.1:5000/data/8', json={"user_name":"ben"})
if res.ok:
    def add_user():
        if add_user():
            conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
            conn.autocommit(True)
            cursor = conn.cursor()
            cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES ("+user_id+","+user_name+",'" + str(datetime.datetime.now()) + "')")
        #     return print(json.loads(y)), {"status": "ok", "user_added": "john"}, 200 # status code
        # else:
        #     return print(json.loads(z)), {"status": "error", "reason": "id already exists"}, 500 # status code
