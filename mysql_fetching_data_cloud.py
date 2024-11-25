import mysql.connector as mc

mydb=mc.connect(host="public_ip",user="mysql_user",password="password",database="company_db")

cur = mydb.cursor()

sql = ''' select * from employees where id=1 '''

cur.execute(sql)

result = cur.fetchall()
print(result)

mydb.close()
