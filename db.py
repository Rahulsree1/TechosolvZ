import sqlite3
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE Data(Id int,ProbId int,Fname varchar(255),Lname varchar(255),email varchar(255),Phone int(15),Problem varchar(1000),status int,Date varchar(20),time varchar(20))")