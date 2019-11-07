import sqlite3
from sqlite3 import Error
try:
   conn=sqlite3.connect("test1.db")
except Error as e:
   print("Cannot open database")
   print(e)
else:
   c=conn.cursor()
   
   c.execute("CREATE TABLE IF NOT EXISTS Student3(id integer primary key,name text not null,department text not null,sem integer not null)")
   
   for i in [(1,"ABC","CSE",5),(11,"XYZ","ISE",3),(34,"PQR","CSE",3),(55,"MNO","ECE",7)]:
     c.execute("INSERT INTO Student3 Values(?,?,?,?)",i)
     
   rows=c.execute("SELECT * FROM Student3 where department='ISE'")
   for i in rows:
      print("ID:",i[0])
      print("NAME:",i[1])
      print("DEPARTMENT:",i[2])
      print("SEMESTER:",i[3])
   
   c.execute("UPDATE Student3 SET name='AAA' where id=12")
   print("--------------------------")
   print("DATABASE after update")
   
   rows=c.execute("SELECT * FROM Student3")
   for i in rows:
      print("ID:",i[0])
      print("NAME:",i[1])
      print("DEPARTMENT:",i[2])
      print("SEMESTER:",i[3])
   
   print("--------------------------")
   c.execute("DELETE FROM Student3 where id=55")
   print("DATABASE after delete")
   rows=c.execute("SELECT * FROM Student3")
   for i in rows:
      print("ID:",i[0])
      print("NAME:",i[1])
      print("DEPARTMENT:",i[2])
      print("SEMESTER:",i[3])  
   conn.commit()
finally:
     conn.close()           
