import sqlite3

connection =sqlite3.connect('student.db')

courser = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARK INT)
"""

courser.execute(table_info)

courser.execute('''INSERT INTO STUDENT VALUES ('Vishal', 'Data Science', 'A',90)''') 
courser.execute('''INSERT INTO STUDENT VALUES ('Pratiksha', 'Data Analyst', 'B',100)''') 
courser.execute('''INSERT INTO STUDENT VALUES ('Karan', 'Devops', 'C',86)''') 
courser.execute('''INSERT INTO STUDENT VALUES ('Kuldipak', 'ML Engineer', 'C',89)''')


# Dispaly all the records
print("The Inserted records are: ")

data = courser.execute('''Select * from STUDENT''')

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()