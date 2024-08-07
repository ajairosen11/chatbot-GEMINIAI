import sqlite3

## Connect to Sqlite
connection=sqlite3.connect("student.db")

## Create a Cursor object to insert record,create table,retrieve
cursor=connection.cursor()

#create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

## Insert Some more Records

cursor.execute('''Insert Into STUDENT values ('Ajai','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values ('Joel','Mech','A',95)''')
cursor.execute('''Insert Into STUDENT values ('Ajith','Mech','B',80)''')
cursor.execute('''Insert Into STUDENT values ('Sajan','Diploma','C',45)''')
cursor.execute('''Insert Into STUDENT values ('Jony','English','D',34)''')

#Display all the records
print('The inserted records are')

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

#Close the connection
connection.commit()
connection.close()