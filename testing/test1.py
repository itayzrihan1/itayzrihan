# import pymysql
#
#
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
# conn.autocommit(True)
# cursor = conn.cursor()
#
# # Inserting data into table
# cursor.execute("INSERT into 12F1HSutPL.dogs (name, age, breed) VALUES ('john', 5, 'husky')")
# cursor.execute("INSERT into 12F1HSutPL.dogs (name, age, breed) VALUES ('rex', 6, 'bulldog')")
# cursor.execute("INSERT into 12F1HSutPL.dogs (name, age, breed) VALUES ('miki', 7, 'pitbull')")
#
# cursor.close()
# conn.close()
#
# import pymysql
#
# # Establishing a connection to DB
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
#
# conn.autocommit(True)
#
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Updating data inside the table
# cursor.execute("UPDATE 12F1HSutPL.dogs SET age = '10' WHERE name = 'rex'")
#
# cursor.close()
# conn.close()
#
#
# import pymysql
#
# # Establishing a connection to DB
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
# conn.autocommit(True)
#
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Deleting data into table
# cursor.execute("DELETE FROM 12F1HSutPL.dogs WHERE name = 'miki'")
#
# cursor.close()
# conn.close()

# import pymysql

# Establishing a connection to DB
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')

# Getting a cursor from Database
# cursor = conn.cursor()

# Getting all data from table “users”
# cursor.execute("SELECT * FROM 12F1HSutPL.dogs;")

# Iterating table and printing all users
# for row in cursor:
#     print(row)

# cursor.close()
# conn.close()

