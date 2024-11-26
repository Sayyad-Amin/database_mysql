import MySQLdb

mydb = MySQLdb.connect(host="18.171.245.36",user="mysql_user",password="Test123@",database="company_db")

cur = mydb.cursor()

sql = ''' INSERT INTO employees (first_name, last_name, age, department, salary, date_of_joining)
VALUES 
    ('Sayyad', 'Amin', 30, 'IT', 75000.00, '2018-05-12') '''
cur.execute(sql)
mydb.commit()
mydb.close()
