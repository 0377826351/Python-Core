# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
# user="root",
# passwd="root")
# print('Connected to MySQL Database')
# cur = myconn.cursor()

# cur.execute("create database testdb")
# cur.execute("show databases")
# for row in cur:
#     print(row)
    
# myconn.close()



# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
# user="root",
# passwd="root",
# db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# cur.execute("""
# CREATE TABLE Employee(
# Code VARCHAR(10) PRIMARY KEY,
# Name VARCHAR(50) NOT NULL,
# Salary FLOAT NOT NULL,
# Department VARCHAR(100) NOT NULL
# )
# """)
# myconn.close()


# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 passwd="root",
#                                 db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# sql = """
# INSERT INTO Employee(Code, Name, Salary, Department)
# VALUES (%s, %s, %s, %s)
# """
# vals = ("PY000007", 'Đỗ Duy Hiệu', 500, "Python 01")
# cur.execute(sql, vals)
# myconn.commit()
# myconn.close()



# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 passwd="root",
#                                 db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# sql = ("""
# INSERT INTO Employee(Code, Name, Salary, Department)
# VALUES (%s, %s, %s, %s)
# """)
# vals = [
# ("PY000009", 'Dương', 700, "Python 01"),
# ("PY000014", 'Trần Hồng Vũ', 1000, "Python 01")
# ]
# cur.executemany(sql, vals)
# myconn.commit()
# myconn.close()



# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 passwd="root",
#                                 db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# cur.execute("SELECT * FROM Employee")
# result = cur.fetchall()
# for row in result:
#     print(row)
# myconn.close()



# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 passwd="root",
#                                 db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# cur.execute("SELECT * FROM Employee WHERE Name LIKE '%Hieu%'")
# result = cur.fetchall()
# for row in result:
#     print(row)
# myconn.close()

# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 passwd="root",
#                                 db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# cur.execute("SELECT * FROM Employee ORDER BY Salary DESC")
# result = cur.fetchone()
# print(result)
# myconn.close()


# import mysql.connector

# myconn = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 passwd="root",
#                                 db = "testdb"
# )
# print('Connected to MySQL Database')
# cur = myconn.cursor()
# cur.execute("UPDATE Employee SET Salary = 600 WHERE Code = 'PY000007'")
# myconn.commit()
# myconn.close()


import mysql.connector

myconn = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root",
                                db = "testdb"
)
print('Connected to MySQL Database')
cur = myconn.cursor()
cur.execute("DELETE FROM Employee WHERE Code = 'PY000007'")
myconn.commit()
myconn.close()  