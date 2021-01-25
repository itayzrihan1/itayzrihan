import pymysql, datetime, requests
# from web_app import users
#
#
# res = requests.post('http://127.0.0.1:5000/users/get_user_data/8', json={"user_name":"johjjjn"})
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
# conn.autocommit(True)
# cursor = conn.cursor()
# cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES ('"+users+"','"+ user_name+",'" + str(datetime.datetime.now()) + "')")
# cursor.close()
# conn.close()
res = requests.post('http://127.0.0.1:5000/data/1', json={"user_name":"john"})
def add_user():
    if res.ok:
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
        conn.autocommit(True)
        cursor = conn.cursor()
        data = res.json()
        r = data['user_id']
        p = data['user_name']
        cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES ('"+r+"','"+ p+",'" + str(datetime.datetime.now()) + "')")
        cursor.close()
        conn.close()
        return print(json.loads(y)), {"status": "ok", "user_added": "john"}, 200 # status code
    else:
        return print(json.loads(z)), {"status": "error", "reason": "id already exists"}, 500 # status code

    # return print(json.loads(y)), {"status": "ok", "user_added": "john"}, 200  # status code
# else:
#     return print(json.loads(z)), {"status": "error", "reason": "id already exists"}, 500  # status code