import mysql.connector as mc

mydb = mc.connect(host="localhost",user="mysql_user",password="Test123@",database="company_db",ssl_disabled=True)

cur = mydb.cursor()

sql = ''' INSERT INTO employees (first_name, last_name, age, department, salary, date_of_joining)
VALUES
    ('Kashif', 'Javed', 28, 'IT', 85000.00, '2019-07-10') '''
cur.execute(sql)
mydb.commit()
mydb.close()
