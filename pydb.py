import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="pavansql"
)

print(mydb)
