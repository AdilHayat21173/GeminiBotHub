import sqlite3

# connected to sqlite database
connection=sqlite3.connect("student.db")
# Create a cursor object to insert record,create table
cursor=connection.cursor()

# Create a table 
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('AdilHayat','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Abubakar','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Maaz','Machine Learning','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ansar','WEB','D',30)''')
cursor.execute('''Insert Into STUDENT values('jalal','Data Engineer','F',8)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()