import mysql.connector
import traceback,sys

try:
    mmdemoDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "mmdemo"
        )

    print(mmdemoDB)

    c = mmdemoDB.cursor()

    # c.execute("Select * from account")

    sql = """SELECT * FROM acxcount WHERE account_type_id > %s
    and name like %s """
    whr = ("1", "%Av%")

    c.execute(sql, whr)
    r = c.fetchall()
    print(len(c.column_names),c.column_names)

    for x in r:
        print (x[1])
        print (len(x))
except:
    print ("O Fuck I have a Mysql issue here...THE NAME OF THE TABLE IS WRONG!!!!.")