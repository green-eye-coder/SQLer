import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table="""
create table student(USN varchar2(20),NAME varchar(30), DEPARTMENT varchar2(25), SEMISISTER varchar2(10),SECTION varchar2(10),MARKS INT);
"""

# cursor.execute(table)

# cursor.execute('''insert into student values('101','Hruthik','Computer Applications','1','A',85)''')
# cursor.execute('''insert into student values('102','Karthik','BTech','3','B',95)''')
# cursor.execute('''insert into student values('103','Amar','Computer Applications','1','A',75)''')
# cursor.execute('''insert into student values('104','Akbar','BTech','3','A',95)''')
# cursor.execute('''insert into student values('105','Anjan','Computer Applications','1','A',70)''')
# cursor.execute('''insert into student values('106','Bhaskar','Computer Applications','1','A',93)''')
# cursor.execute('''insert into student values('107','Champaka','Computer Applications','1','B',75)''')
# cursor.execute('''insert into student values('108','Dhanush','BTech','3','A',75)''')
# cursor.execute('''insert into student values('109','Amar','BTech','3','A',67)''')
# cursor.execute('''insert into student values('110','Raju','Computer Applications','1','B',75)''')
# cursor.execute('''insert into student values('111','Ram charan','Computer Applications','1','B',80)''')
# cursor.execute('''insert into student values('112','Ravi','Computer Applications','1','B',73)''')
# cursor.execute('''insert into student values('113','Sahana','Computer Applications','1','B',96)''')
# cursor.execute('''insert into student values('114','Savjanya','Computer Applications','1','B',93)''')



# data=cursor.execute('''select * from student''')
data=cursor.execute('''SELECT *,MAX(marks) FROM STUDENT where department='BTech'  ;''')
# cursor.execute('''drop table student''')
for row in data:
    print(row)


connection.commit()
connection.close()