import mysql.connector as mysql

try:
    myDB = mysql.connect(host="rds-engg-shared-mysql.cma1vpsbcibq.us-east-2.rds.amazonaws.com", port=3306, user="admin", password="mYsQlAdm1nU$er2020#")

    connected = myDB.is_connected()
    print(connected)
    if not connected:
        myDB.ping(True)

    myCursor = myDB.cursor()

    myCursor.execute("CREATE DATABASE mydatabase")

    myCursor.execute("SHOW DATABASES")

    for x in myCursor:
        print(x)
except Exception as e:
    print("Failed due to " + e)


# class MysqlDB:
#
#     # def __init__(self, hostname, port, username, password):
#     #     self.hostname = hostname
#     #     self.port = port
#     #     self.username = username
#     #     self.password = password
#
#     def connect_db(self, hostname, port, username, password):
#         return mysql.connector.connect(self.hostname, self.port, self.username, self.password)
#
#
# obj = MysqlDB()
# my = obj.connect_db("rds-engg-shared-mysql.cma1vpsbcibq.us-east-2.rds.amazonaws.com", 3306, "admin", "mYsQlAdm1nU$er2020#")
# myCursor = my.cursor()
# myCursor.execute("create database tejeshQA")
#
#
#
#
