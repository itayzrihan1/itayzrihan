# # import requests
# # from flask-test import users
# # # res =  requests.get("https://api.exchangeratesapi.io/latest?base=USD")
# # # data = res.json()
# # # results = data['rates']
# # # currency_value = results['ILS']
# # # x = float(input("Please enter an amount of Shekeles to convert to Dollars: "))
# # # print(x * currency_value)
# #
# # res = requests.post('http://127.0.0.1:5000/data/8', json={"user_name":"ben"})
# # if res.ok:
# #     def add_user():
# #         if add_user():
# #             conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
# #             conn.autocommit(True)
# #             cursor = conn.cursor()
# #             cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES ("+user_id+","+user_name+",'" + str(datetime.datetime.now()) + "')")
# #         #     return print(json.loads(y)), {"status": "ok", "user_added": "john"}, 200 # status code
# #         # else:
# #         #     return print(json.loads(z)), {"status": "error", "reason": "id already exists"}, 500 # status code
#
# # import requests
# # res = requests.post('http://127.0.0.1:5000/data/1', json={"user_name":"itay"})
# # if res.ok:
# #     print(res.json())
# # import pymysql,requests,datetime,time
# #
# # import requests
# #
# # res = requests.get("http://127.0.0.1:5000/data/1")
# # data = res.json()
# # id = data["user_id"]
# # name = data["user_name"]
# # conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP',db='12F1HSutPL')
# # conn.autocommit(True)
# # cursor = conn.cursor()
# # now = datetime.datetime.utcnow()
# # cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES (%s,%s,%s)" , (id, name, now.strftime('%Y-%m-%d %H:%M:%S')))
# #
# #
#
# import pymysql
#
# # Establishing a connection to DB
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
#
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Getting all data from table “users”
# cursor.execute("SELECT * FROM 12F1HSutPL.users;")
#
# # Iterating table and printing all users
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()

