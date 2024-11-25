import mysql.connector as mc

mydb=mc.connect(host="localhost",user="root",password="password",database="company_db",ssl_disabled=True)

cur = mydb.cursor()

sql = ''' select * from employees where id=1 '''

cur.execute(sql)

result = cur.fetchall()
print(result)

mydb.close()
